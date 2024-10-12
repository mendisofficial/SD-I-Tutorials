# Savings Goal Tracker

saving_goal = float(input("Enter your saving goal: "))
current_amount = float(input("Enter your current amount: "))

monthly_savings_amount = float(input("Enter monthly savings amount: "))

months = (saving_goal - current_amount) / monthly_savings_amount

print(f"Months to reach goal: {months:.0f}")