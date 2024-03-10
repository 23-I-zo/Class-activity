#Initializing an empty list and dictionary
student_list = []
student_dic = {}

#promt users to add their name, age and grade
name = input("Enter your name: ")
age = input("Enter your age:")
grade = input("Enter your grade: ")
student_list.append(name)
student_dic[name] = {"age":age, "grade": grade}
print("Yor information has been successfully added!")
print(student_dic.items())

#Searching students by name
Student_name = input("Enter the name of the student you are searching: ")
if Student_name in student_list:
    print(f"Student found!: {student_dic[Student_name]} ")
else:
    print("Student not found!")

#Removing Students
student_remove = input("Enter the name of the student that you want to remove: ")
if student_remove in student_list:
    remove_detail = student_dic[student_remove]
    student_list.remove(student_remove)
    del student_dic[student_remove]
    print("Student removed successfully")
    print("Students avialable:", student_list)

else:
    print("Student not found")