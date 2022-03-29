class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating isinstance Attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400

# print(harry.company)
# print(rajni.company)
# Employee.company = "YouTube"
# print(harry.company)
# print(rajni.company)  


harry.salary = 45 
print(harry.salary)
print(rajni.salary) 

 # Below line throws an error an address is not present in isinstance/class
# print(rajni.address)