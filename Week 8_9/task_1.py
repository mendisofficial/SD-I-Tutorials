# Read a File and Count Characters
# Write a Python program that opens a file named input.txt, reads its content, and prints the total number of characters in the file.

file = open("input.txt", "r")
content = file.read()
file.close()

print("Total number of characters in the file: ", len(content))
