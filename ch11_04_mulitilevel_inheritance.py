class Person :
    def __init_(self):
        super().__init__()
    country = "India"
    def takeBreak(self):
        print("I am breathing..")


class Employee(Person):
    company = "Honda"


    def __init__(self):
        super(). __init__()
        print("Initializing Person...\n")


    def getSalary(self):
        print(f" salary is {self.salary}")


    def takeBreath(self):
        super().takeBreak()
        print("I am an Employee so i am luckily breathing...")


def Programmer(Employee):
    company = "Fiverr"


    def getSalary(self):
        print(f"No salary to programmers")


    def takeBreath(self):
       # super().takeBreath()
        print("I am an Employee so I am  breathing++...")    


p = Person()
p. takeBreath()
print(p.company)  # throws an error

e = Employee()
e.takeBreath()
# print(e.company)

pr = Programmer()                    
pr.takeBreath()