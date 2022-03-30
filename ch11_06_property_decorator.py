class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonuus = 400
    # totalSalary = 6100


    @property
    def totalSalary(self):
        return self.salary + self.salarybonuus

    @totalSalary.setter
    def totalSalary(self, Va1):
        self.salarybonuus = Va1 - self.salary    


e = Employee()
print(e.totalSalary)      
e.totalSalary = 5800 
print(e.salary)
print(e.salarybonuus)