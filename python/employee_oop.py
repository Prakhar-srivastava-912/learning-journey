class Employee:
    company="OpenAI"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name of company is",self.company)
        print("Name of employee is",self.name)
        print("Salary of employee is",self.salary)
s=Employee("Prakhar",50000)
s.display()
p=Employee("Rahul",65000)
p.display()
