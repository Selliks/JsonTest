import json
# У файлі 10_company.json зберігаються дані про компанію: назва, список відділів
# (кожен відділ має ім’я та список працівників, які мають ім’я, посаду та зарплату).

with open("company.json", "r") as file:
    data = json.load(file)


def avg_salary(data):
    return {
        dept["name"]: sum(emp["salary"] for emp in dept["employees"]) / len(dept["employees"])
        for dept in data["departments"] if dept["employees"]
    }


def filter_salary(data, threshold):
    return [
        {"name": emp["name"], "position": emp["position"], "department": dept["name"], "salary": emp["salary"]}
        for dept in data["departments"] for emp in dept["employees"] if emp["salary"] > threshold
    ]


def add_emp(data, department_name, employee):
    for dept in data["departments"]:
        if dept["name"] == department_name:
            dept["employees"].append(employee)
            return True
    return False


avg_salaries = avg_salary(data)
high_salary_employees = filter_salary(data, 35000)

print(f"Average Salaries: {avg_salaries} \n---\nEmployees with High Salary: {high_salary_employees}")


if add_emp(data, "Training Unit", {"name": "Ivan Novikov", "position": "Trainee", "salary": 30000}):
    print("Employee added successfully.")

with open("company.json", "w") as file:
    json.dump(data, file, indent=4)
