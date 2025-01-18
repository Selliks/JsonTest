import json

manage = {
    "first name": "Kevin",
    "last name": "Levrone",
    "age": 60,
    "placement": "Baltimore",
}

with open("1_person.json", "w", encoding="utf-8") as f:
    json.dump(manage, f, ensure_ascii=False, indent=4)