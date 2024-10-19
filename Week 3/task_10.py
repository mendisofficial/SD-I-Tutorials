# Advanced Grade Calculation System

coursework = float(input("Enter your coursework mark: "))

if coursework < 0 or coursework > 100:
    print("Invalid mark.")
    exit()

mid_exam = float(input("Enter your midterm exam mark: "))

if mid_exam < 0 or mid_exam > 100:
    print("Invalid mark.")
    exit()

final_exam = float(input("Enter your final exam mark: "))

if final_exam < 0 or final_exam > 100:
    print("Invalid mark.")
    exit()

graded_coursework = coursework * 0.4
graded_mid_exam = mid_exam * 0.25
graded_final_exam = final_exam * 0.35

total_mark = graded_coursework + graded_mid_exam + graded_final_exam

if 70 <= total_mark <= 100:
    grade = "A"
elif 50 <= total_mark <= 69:
    grade = "B"
elif 40 <= total_mark <= 49:
    grade = "C"
else:
    grade = "F"

print(f"Graded Coursework mark: {graded_coursework:.2f}\nGraded Midterm exam mark: {graded_mid_exam:.2f}\nGraded Final exam mark: {graded_final_exam:.2f}")
print(f"Total mark: {total_mark:.2f}\nGrade: {grade}")