# Tax Calculator Based on Gross Income

gross_income = float(input("Enter your gross income: "))
tax_rate = 0
tax_amount = 0

if 12500 < gross_income <= 50000:
    tax_rate = 0.2
    tax_amount = gross_income * tax_rate
    print(f"Tax rate: {tax_rate}\nTax amount: {tax_amount}")

elif 50000 < gross_income <= 150000:
    tax_rate = 0.4
    tax_amount = gross_income * tax_rate
    print(f"Tax rate: {tax_rate}\nTax amount: {tax_amount}")

elif gross_income > 150000:
    tax_rate = 0.45
    tax_amount = gross_income * tax_rate
    print(f"Tax rate: {tax_rate}\nTax amount: {tax_amount}")

else:
    print("No tax applied.")

net_income = gross_income - tax_amount
print(f"Net income: {net_income}")