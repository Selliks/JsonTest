import json

products = [
    {"name": "Laptop", "price": 1200, "quantity": 5},
    {"name": "Smartphone", "price": 300, "quantity": 9},
    {"name": "Headphones", "price": 100, "quantity": 12},
    {"name": "Monitor", "price": 300, "quantity": 5},
    {"name": "Keyboard", "price": 70, "quantity": 5}
]

with open("5_products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=4)

try:
    with open("5_products.json", "r", encoding="utf-8") as file:
        products = json.load(file)

    total_cost = sum(product["price"] * product["quantity"] for product in products)
    print(f"Total price: {total_cost}$")

except (FileNotFoundError, json.JSONDecodeError):
    print("Error. Not completed")
