marks  = int(input("Enter your Marks\n"))


if(marks>=90):
    grade = "Ex"
elif marks>=80:
    grade = "A" 
elif marks>=70:
    grade = "b" 
elif marks>=60:
    grade = "c"  
elif marks<50:
    grade = "f" 
            
print("Your grade is " + grade)            