from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from image_search import find_similar

app = Flask(__name__)

# Load dataset
DATASET_PATH = os.path.join("static", "en.openfoodfacts.org.products.tsv")
df = pd.read_csv(DATASET_PATH, sep="\t", dtype=str, low_memory=False)

def get_product_info(barcode):
    """Look up product info by barcode in the TSV dataset."""
    product = df[df['code'] == barcode].fillna("Unknown")
    if not product.empty:
        product = product.iloc[0]
        return {
            'product_name': product.get('product_name', 'Unknown'),
            'brands': product.get('brands', 'Unknown'),
            'nutriments': {
                'energy_100g': product.get('energy_100g', 'Unknown'),
                'fat_100g': product.get('fat_100g', 'Unknown'),
                'sugars_100g': product.get('sugars_100g', 'Unknown'),
                'proteins_100g': product.get('proteins_100g', 'Unknown')
            },
            'image_url': product.get('image_url', '')
        }
    return None

@app.route('/')
def index():
    """Homepage: barcode search + image upload form"""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """Search by barcode"""
    barcode = request.form.get('barcode', '').strip()
    if barcode:
        info = get_product_info(barcode)
        if info:
            return render_template('result.html', info=info)
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    """Search by uploaded image"""
    uploaded_file = request.files.get('image')
    if not uploaded_file or uploaded_file.filename == "":
        return redirect(url_for('index'))

    # Save temp image
    temp_path = "temp_upload.jpg"
    uploaded_file.save(temp_path)

    # Run AI similarity search
    similar_barcode = find_similar(temp_path)

    # Cleanup
    os.remove(temp_path)

    if similar_barcode:
        info = get_product_info(similar_barcode)
        if info:
            return render_template("result.html", info=info)

    return render_template("not_found.html")

if __name__ == '__main__':
    # Run so we can access from Mac & iPhone on same WiFi
    app.run(host="0.0.0.0", port=5001, debug=True)
  