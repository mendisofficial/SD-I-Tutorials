# Use if-elif-else to categorize a number as 'Negative', 'Zero', or 'Positive'.

number = int(input("Enter a number: "))
if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
else:
    print("Positive")
