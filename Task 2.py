class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old and I am studying {self.course}.")


student1 = Student("Jasmin", 22, "Nursing")
student2 = Student("Lorentz", 21, "Information Technology")
student3 = Student("Lloyd", 22, "Radiologic Technology")

print("Student 1 Intorduction:")
student1.introduce()
print("\nStudent 2 Intorduction:")
student2.introduce()
print("\nStudent 3 Intorduction:")
student3.introduce()
