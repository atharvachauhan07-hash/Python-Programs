print(" program to calculate grades of a student ")
marks = float(input("Enter the student's marks (out of 100): "))

if marks >= 90:
    grade = "O"
elif marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "B+"
elif marks >= 50:
    grade = "B"
elif marks >= 40:
    grade = "C"
elif marks >= 30:
    grade = "D"
else:
    grade = "F (Fail)"

print("Marks:", marks)
print("Grade:", grade)
