#6. Create a base class called Employee with properties name and salary.
#  Create a derived class called Manager that inherits from Employee and 
# adds property department. Write a method in Manager to display the name,
#  salary and department of the manager.



class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


m1 = Manager("Virat", 90000, "Tech")
m1.display()

