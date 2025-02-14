
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


employee = Employee("Paul", "Drug Lord", 7000000)
employee.give_raise(5000)
employee.display_employee()