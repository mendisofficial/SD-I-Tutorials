# Line by Line Analysis
# Given a text file named data.txt, write a Python program to read the file line by line and print each line with its corresponding length (number of characters).

file = open("data.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    print(line, len(line))
