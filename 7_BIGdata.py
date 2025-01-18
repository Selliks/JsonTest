import ijson

try:
    with open('7_large_data.json', 'r', encoding='utf-8') as file:
        objects = ijson.items(file, 'item')

        for product in objects:
            if product.get("price", 0) > 1000:
                print(f"Назва: {product['name']}, Ціна: {product['price']}, Кількість: {product['quantity']}")

except (FileNotFoundError, ijson.JSONDecodeError):
    print("Error. Not completed")
