class Employee:
    company = "Google"

    def __init__(self,name,salary,submit):
        self.name = name
        self.salary = 100
        self.submit = submit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employ is {self.salary}")
        print(f"The submit of the employee is {self.submit}")    

    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature} ")

    @staticmethod
    def greet():
        print("Good Moring, sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")    

harry = Employee("Harry", 100 , "YouTube")   
harry.getDetails()     

