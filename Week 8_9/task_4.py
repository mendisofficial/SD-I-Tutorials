# Find and Replace in File
# Write a Python program that reads a file named story.txt, finds all occurrences of the word "Python" and replaces them with "Pythons". Save the modified content into a new file called modified_story.txt.

file = open("story.txt", "r")
content = file.read()
file.close()

modified_content = content.replace("Python", "Pythons")

file = open("modified_story.txt", "w")
file.write(modified_content)
file.close()