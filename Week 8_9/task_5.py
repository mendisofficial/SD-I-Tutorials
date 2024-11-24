# Generating a Summary Report
# You have a text file reviews.txt where each line contains a product review followed by a rating out of 5 (e.g., This product works well, 4). Write a Python script to read the file and generate a summary report in a new file summary.txt that contains the average rating and the total number of reviews.

file = open("reviews.txt", "r")
lines = file.readlines()
file.close()

total_reviews = 0
total_rating = 0

for line in lines:
    review, rating = line.split(", ")
    total_reviews += 1
    total_rating += int(rating)

average_rating = total_rating / total_reviews

file = open("summary.txt", "w")
file.write("Average Rating: " + str(average_rating) + "\n")
file.write("Total Number of Reviews: " + str(total_reviews))
file.close()
