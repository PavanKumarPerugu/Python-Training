def calculate_bonus(salary, rating):
    if rating > 8:
        bonus = salary * 0.2
    elif rating > 5:
        bonus = salary * 0.1
    else:
        bonus = salary * 0.05
    return bonus


def total_salary(salary, rating, deductions):
    bonus = calculate_bonus(salary, rating)
    total = salary + bonus - deductions
    return total


# Sample test data
employees = [
    {"name": "Alice", "salary": 50000, "rating": 9, "deductions": 2000},
    {"name": "Bob", "salary": 40000, "rating": 4, "deductions": 1000},
    {"name": "Charlie", "salary": 60000, "rating": 7, "deductions": 5000},
]

for emp in employees:
    total = total_salary(emp["salary"], emp["rating"], emp["deductions"])
    print(f"{emp['name']} total salary: ₹{total}")
