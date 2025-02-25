class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

# Creating three student objects
student1 = Student("Charmaine Villanueva", 20, "DIP-IT II")
student2 = Student("Ariel Lacambra", 25, "DIP-IT II")
student3 = Student("Nikka Jane Senado", 21, "DIP-IT II")

# Calling the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()
