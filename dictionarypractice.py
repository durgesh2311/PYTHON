#1.
student_info = {'durgesh':89,'yash':95,'bob':78,'harshal':67,'david':90}
print(student_info)

#2.
print("Marks of durgesh:", student_info['durgesh'])

#3.
student_info["Priya"] = 95
print(student_info)

#4.
student_info['durgesh'] = 90
print(student_info)

#5.
del student_info['durgesh']
print(student_info)

#6.
print("Student Names:")
print(student_info.keys())

#7.
print("\nStudent Marks:")
print(student_info.values())

#8.
print("\nStudents and their Marks:")
for name, marks in student_info.items():
    print(name, ":", marks)

#9. 
student_name = "priya"
if student_name in student_info:
    print("\n", student_name, "is present in the dictionary")
else:
    print("\n", student_name, "is NOT present in the dictionary")    

#10.
mark = 95
if mark in student_info.values():
    print(mark, "is present in the dictionary values")
else:
    print(mark, "is NOT present in the dictionary values")    

#11.
print("Marks of durgesh:", student_info.get("durgesh", "Student not found"))
print("Marks of bob:", student_info.get("bob", "Student not found"))    

#12.
employees = {
    "Anil": "HR",
    "Sunita": "Finance",
    "Rohit": "IT",
    "Meena": "Marketing"
}

print(employees)

#13.
print("\nDepartment of Rohit:", employees["Rohit"])

#14.
employees["Karan"] = "Operations"
print(employees)

#15.
employees["Sunita"] = "HR"
print(employees)

#16.
del employees["Meena"]
print(employees)

#17.
print("\nSorted by employee names (Ascending):")
for name in sorted(employees.keys()):
    print(name, ":", employees[name])

#18.
print("\nSorted by department names (Ascending):")
for name, dept in sorted(employees.items(), key=lambda x: x[1]):
    print(name, ":", dept)

#19.
print("\nSorted by employee names (Descending):")
for name in sorted(employees.keys(), reverse=True):
    print(name, ":", employees[name])    

#20.
print("\nSorted by department names (Descending):")
for name, dept in sorted(employees.items(), key=lambda x: x[1], reverse=True):
    print(name, ":", dept)

students_marks = {
    "Amit": 85,
    "Riya": 92,
    "Sohan": 78,
    "Neha": 88,
    "Rahul": 90
}

# 21.
value_to_find = 88
keys_with_value = [k for k, v in students_marks.items() if v == value_to_find]
print("Keys with value", value_to_find, ":", keys_with_value)


# 22.
count = 0
for marks in students_marks.values():
    if marks > 80:
        count += 1
print("Students scoring above 80:", count)


# 23.
students = {
    "Amit": {"age": 20, "grade": "A", "department": "Science"},
    "Riya": {"age": 21, "grade": "A+", "department": "Commerce"},
    "Sohan": {"age": 19, "grade": "B", "department": "Arts"}
}

# 24.
print("Grade of Riya:", students["Riya"]["grade"])


# 25. 
students["Sohan"]["department"] = "Science"


# 26.
print("\nStudent Names and Grades:")
for name, details in students.items():
    print(name, ":", details["grade"])


# 27.
students_group1 = {"Amit": 85, "Riya": 92}
students_group2 = {"Neha": 88, "Rahul": 90}

merged_students = students_group1 | students_group2
print("\nMerged Dictionary:", merged_students)


# 28.
students_group1.clear()
print("After clearing:", students_group1)


# 29.
original = {"A": 10, "B": 20}
copied = original.copy()
copied["A"] = 100

print("\nOriginal Dictionary:", original)
print("Copied Dictionary:", copied)


# 30.
squares = {}
for i in range(1, 6):
    squares[i] = i * i

print("\nDictionary of numbers and squares:", squares)
    

