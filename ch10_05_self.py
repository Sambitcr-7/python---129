class Employee:
      company  = "Google"
      def getSalary(self):
        print(f"Salary for this employee working in {self.company} is{self.salary}")

harry = Employee()
# harry.getSalary()
harry.salary = 10000
# harry.getSalary(harry)  
harry.getSalary() # Employee.getSalary(harry)      

