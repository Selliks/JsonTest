import json
import re

# invalid_json_data = """
# {
#     "name": "Product 1",
#     "price": 1500,
#     "quantity": 5,
#     "details": { "brand": "BrandX", "color": "Red" }  // Некоректний коментар
# }
# """
# with open('8_unknown.json', 'w', encoding='utf-8') as f:
#     json.dump(invalid_json_data, f, ensure_ascii=False, indent=4)


def remove_comments(json_string):
    return re.sub(r'//.*?(\n|$)', '', json_string)


def is_valid_json(json_string):
    try:

        json_string = remove_comments(json_string)
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False


try:
    with open('8_unknown.json', 'r', encoding='utf-8') as f:
        json_data = f.read()

    if is_valid_json(json_data):
        print("JSON is correct.")
    else:
        print("JSON is incorrect.")

except FileNotFoundError:
    print("Not Found.")
