# Simple Interest Calculator

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest: {simple_interest}")
