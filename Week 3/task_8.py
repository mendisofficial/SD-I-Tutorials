# Implement a nested if-else structure to calculate different types of discounts based on purchase amount: above 1000, 10% discount; between 500 and 1000, 5% discount; below 500, no discount.

purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount > 1000:
    discount = 0.1
    final_amount = purchase_amount - (purchase_amount * discount)
    print(f"10% discount applied. Final amount: {final_amount}")
elif purchase_amount >= 500:
    discount = 0.05
    final_amount = purchase_amount - (purchase_amount * discount)
    print(f"5% discount applied. Final amount: {final_amount}")
else:
    print("No discount applied.")
