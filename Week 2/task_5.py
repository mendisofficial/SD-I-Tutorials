# Grade Calculator

subject_1 = float(input("Enter the mark for subject 1: "))
subject_2 = float(input("Enter the mark for subject 2: "))
subject_3 = float(input("Enter the mark for subject 3: "))
subject_4 = float(input("Enter the mark for subject 4: "))
subject_5 = float(input("Enter the mark for subject 5: "))

average = (subject_1 + subject_2 + subject_3 + subject_4 + subject_5) / 5

if average >= 75:
    grade = "A"
elif average >= 65:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 35:
    grade = "S"
else:
    grade = "F"

print(f"Average: {average:.2f} \nGrade: {grade}")