# Salary Increase Calculator

current_salary = float(input("Enter the current salary: "))

percentage_increase = float(input("Enter the percentage increase: "))

new_salary = current_salary + (current_salary * percentage_increase / 100)

print(f"New Salary: {new_salary:.2f}")
