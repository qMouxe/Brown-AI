class Registry:
    def __init__(student, gender, age, name):
        student.gender = gender
        student.age = age
        student.name = name

    def fun1(student):
        print("Student name: " + student.name + " Gender: " + student.gender + " Age: " + str(student.age))

stu1 = Registry("Male", 16, "Seymour")
stu1.fun1()