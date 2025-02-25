class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"{self.name} received a raise of ${amount}. New salary: ${self.salary}")
        else:
            print("Raise amount must be positive.")

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: ${self.salary}")

# Creating an employee object
employee = Employee("Charmaine Villanueva", "I.T. Support", 70000)

# Giving the employee a raise
employee.give_raise(5000)

# Displaying employee details
employee.display_employee()
