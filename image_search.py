import pickle
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np

# Load embeddings
with open("embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

# Load ResNet18
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model = torch.nn.Sequential(*list(model.children())[:-1])
model.eval()

# Image transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def find_similar(image_path):
    image = Image.open(image_path).convert("RGB")
    tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        query_embedding = model(tensor).squeeze().numpy()

    best_match = None
    best_score = float("inf")

    for code, emb in embeddings.items():
        dist = np.linalg.norm(query_embedding - emb)
        if dist < best_score:
            best_score = dist
            best_match = code

    return best_match
