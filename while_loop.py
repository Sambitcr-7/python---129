# syntax and Flowchart
i = 1
while i < 5:
    print(i)
    i = i + 1


# conditional statement
x = 1
while x <= 5:
    if x == 3:
        x = x + 1
        continue
    else:
        print(x)
        x = x + 1 


# infinte while Loop 
i = 1

while i < 10:
    print(i)
    i+= 1


# Nested While Loop 
i = int(input("enter a number"))

while i < 10:
    while i == 5:
        print(i)
        i = i + 1



# exp (2)       
i = 0
j = 5

while i < 6:
    while j > 0:
        print(i, j)
        i = i + 1
        j = j - 1



# EXP (3)
i = 'edureka'
j = 1


while j > 0:
    for x in i:
        print(j , i)
        j = j + 1
    if x == 'a':
        break    




# exp(4)
i = 'edureka'
j = 1
while j < 8:
    for x in i :
        print(j , x)
        j + j + 1
        if x == 'a':
            break    