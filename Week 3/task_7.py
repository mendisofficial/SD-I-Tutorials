# Develop a program that categorizes a character as 'Lowercase', 'Uppercase', 'Digit', or 'Special Character'.

character = input("Enter a character: ")

if character.islower():
    print("Lowercase")
elif character.isupper():
    print("Uppercase")
elif character.isdigit():
    print("Digit")
else:
    print("Special Character")
