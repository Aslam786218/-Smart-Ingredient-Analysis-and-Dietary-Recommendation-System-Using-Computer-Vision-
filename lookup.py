import pandas as pd
import os

# Load OpenFoodFacts dataset once
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'static', 'en.openfoodfacts.org.products.tsv')
df = pd.read_csv(file_path, sep='\t', low_memory=False)

def lookup_product(code):
    result = df[df['code'] == str(code)]
    if result.empty:
        return None
    product = result.iloc[0]
    return {
        'product_name': product.get('product_name', 'Unknown'),
        'brands': product.get('brands', 'Unknown'),
        'nutriments': {
            'energy_100g': product.get('energy_100g'),
            'fat_100g': product.get('fat_100g'),
            'sugars_100g': product.get('sugars_100g'),
            'proteins_100g': product.get('proteins_100g'),
        },
        'image_url': product.get('image_url', None)
    }
