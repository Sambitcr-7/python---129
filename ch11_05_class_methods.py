class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"
    
    @classmethod
    def changeSalary(cls,sa1):
        cls.salary  = sa1


e = Employee()
print(e.salary)  
e.changeSalary(455) 
print(e.salary)
print(Employee.salary) 