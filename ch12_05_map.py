def square(num):
    return num*num

l = [1,2,4]

# Method l
l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# Method 2
print(map(square,l))