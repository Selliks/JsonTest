import json

with open('1_person.json', 'r', encoding='utf-8') as f:
    read = json.load(f)

print(read)
