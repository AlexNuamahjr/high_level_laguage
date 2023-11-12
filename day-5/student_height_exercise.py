student_heights = input("Input a list of student heights: ").split()
for i in range(0, len( student_heights)):
    student_heights[i] = int(student_heights[i])
# print(student_heights)
# sum of student heights
total_height = 0
for height in student_heights:
    total_height += height
# print(total_height)
# total number of students
total_students = 0
for student in student_heights:
    total_students += 1
# print(total_students)
# average student height
average_height = round(total_height / total_students)
print(f"The average student height is {average_height}")

