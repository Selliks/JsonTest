import json

students = [
    {"name": "John Smith", "age": 20, "average_score": 95},
    {"name": "Alice Brown", "age": 22, "average_score": 88},
    {"name": "Emily Davis", "age": 19, "average_score": 91},
    {"name": "Michael Lee", "age": 21, "average_score": 85},
]

with open("4_students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)


try:
    with open("4_students.json", "r", encoding="utf-8") as file:
        students = json.load(file)

    top_students = [i for i in students if i.get("average_score", 0) > 90]

    for student in top_students:
        print(f"Name: {student['name']}, Age: {student['age']}, Average score: {student['average_score']}")

except (FileNotFoundError, json.JSONDecodeError):
    print("Error. Not completed")
