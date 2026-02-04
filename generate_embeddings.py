# generate_embeddings.py (demo-images version)
import os
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import pickle
from tqdm import tqdm

IMAGE_FOLDER = "demo_images"
OUTPUT_FILE = "embeddings.pkl"

print("Loading ResNet18 model...")
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model = torch.nn.Sequential(*list(model.children())[:-1])
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

embeddings = {}
if not os.path.isdir(IMAGE_FOLDER):
    raise SystemExit(f"Folder {IMAGE_FOLDER} does not exist. Create it and add demo images named by barcode.")

for filename in tqdm(os.listdir(IMAGE_FOLDER)):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(IMAGE_FOLDER, filename)
        try:
            image = Image.open(path).convert("RGB")
            tensor = transform(image).unsqueeze(0)
            with torch.no_grad():
                emb = model(tensor).squeeze().numpy()
            code = os.path.splitext(filename)[0]  # filename without ext
            embeddings[code] = emb
        except Exception as e:
            print("Skipping", filename, "error:", e)

with open(OUTPUT_FILE, "wb") as f:
    pickle.dump(embeddings, f)

print(f"Saved {len(embeddings)} embeddings to {OUTPUT_FILE}")
