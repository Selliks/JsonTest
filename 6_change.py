import json

try:
    with open('5_products.json', 'r', encoding='utf-8') as f:
        products = json.load(f)

    if not isinstance(products, list) or not all(isinstance(product, dict) for product in products):
        raise ValueError("Not typical data type")

except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
    print(f"Error. {e}")
    products = []

for product in products:
    if product.get("name") == "Laptop":
        product["quantity"] = 9

new_product = {"name": "Mouse", "price": 100, "quantity": 5}
products.append(new_product)

with open("5_products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=4)

