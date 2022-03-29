class Employee:
    company = "Google"

    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature} ")

    @staticmethod
    def greet():
        print("Good Moring, sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")    

harry = Employee()
harry.salary =10000
harry.getSalary("Thanks!") # Employee.getSalary(harry)          
harry.greet() # Employee.greet()
harry.time()