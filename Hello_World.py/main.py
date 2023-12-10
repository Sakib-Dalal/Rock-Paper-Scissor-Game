student_heights = input("Enter height: ").split()  # Using .split function to split the input into list
print(f"split function: {student_heights}")
print(f"data type of student_height {type(student_heights)}")
print(f"length of student_height list: {len(student_heights)}")

length_of_list = len(student_heights)

add = 0

for n in student_heights:
    add = int(n) + add

avg = round(add/length_of_list)
print(f"Total of students_height: {add}")
print(f"Total Students: {length_of_list}")
print(f"average height of student are: {avg}")
