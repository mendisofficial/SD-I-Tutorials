# Write a program to determine whether a character entered is a vowel or consonant.

character = input("Enter a character: ")

if character in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
