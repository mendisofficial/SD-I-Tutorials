# File Content Manipulation
# Create a Python program that reads a file named article.txt, performs the following transformations, and writes the output to a new file called formatted_article.txt
# Replace all instances of a specified word with another word provided by the user.
# Ensure all sentences start with a capital letter.
# Remove all leading and trailing whitespace from each line.

file = open("article.txt", "r")
content = file.readlines()
file.close()

word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")

formatted_content = []

for line in content:
    line = line.strip()
    if line:
        if line[0].islower():
            line = line.capitalize()
        line = line.replace(word_to_replace, replacement_word)
        formatted_content.append(line)

file = open("formatted_article.txt", "w")
file.write("\n".join(formatted_content))
file.close()