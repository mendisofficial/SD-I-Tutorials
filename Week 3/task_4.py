# Write a nested if-else program that checks if a number is less than 10. If it is, check if it is even or odd and print the result.

number = int(input("Enter a number: "))

if number < 10:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Number is greater than 10")
