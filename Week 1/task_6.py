# Basic Arithmetic Calculator

input1 = int(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
input2 = int(input("Enter the second number: "))

if operation == "+":
    print(f"Result : {input1 + input2}")

elif operation == "-":
    print(f"Result : {input1 - input2}")

elif operation == "*":
    print(f"Result : {input1 * input2}")

elif operation == "/":
    print(f"Result : {input1 / input2}")

else:
    print("Invalid operation")
