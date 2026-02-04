🥗 AI-Driven Food & Nutrition Scanner

An AI-powered web application that helps users identify packaged food products and analyze their nutritional information using barcode scanning and image-based food recognition.
Built as a college/demo project with a focus on real-world health and nutrition use cases.

🚀 Features

->Barcode-based food lookup using the Open Food Facts dataset
->Image-based product search using AI similarity matching
->AI-assisted nutrition analysis (energy, fat, sugar, protein)
->Clean and user-friendly web interface
->Accessible from mobile devices on the same Wi-Fi network
->Fallback from barcode → image recognition

🛠️ Tech Stack\

->Backend: Python, Flask
->Data Processing: Pandas
->Dataset: Open Food Facts (TSV)
->AI / ML: Image embeddings & similarity search
->Frontend: HTML, CSS (Flask templates)
->Environment: Conda (Miniforge)

## ▶️ Running the Project (Terminal Guide)

### ✅ Prerequisites
- Python **3.9+** (recommended: 3.10)
- Conda / Miniforge **or** standard Python + pip
- Minimum **4–6 GB RAM** (dataset is large)

---

## 🍎 macOS / Linux Setup

1. Navigate to the project directory
```bash
cd "/Users/Shared/Food AI/food-ai-prototype"

2. conda create -n facenv python=3.10
conda activate facenv

3. pip install flask pandas numpy pillow scikit-learn

4. Download
en.openfoodfacts.org.products.tsv
and place it inside:

food-ai-prototype/static/

5. python generate_embeddings.py

6. python app.py

7. Open in browser
http://localhost:5001

🪟 Windows Setup
1. Open Anaconda Prompt or Command Prompt

2. Navigate to the project directory
cd C:\Users\<your-username>\food-ai-prototype


⚠️ Avoid spaces in folder names on Windows if possible.

3. Create and activate Conda environment
conda create -n facenv python=3.10
conda activate facenv

4. Install dependencies
pip install flask pandas numpy pillow scikit-learn

5. Add dataset
Place
en.openfoodfacts.org.products.tsv
inside:

food-ai-prototype\static\

6. (Optional) Generate image embeddings
python generate_embeddings.py

7. Run the Flask application
python app.py

Open browser:
http://127.0.0.1:5001