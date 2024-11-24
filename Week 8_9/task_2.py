# Write Strings to a File
# Create a Python script that writes the strings "Hello" and "World" on two separate lines in a file named greetings.txt.

file = open("greetings.txt", "w")
file.write("Hello\n")
file.write("World")
file.close()
