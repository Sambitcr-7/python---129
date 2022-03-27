# Creating an empty set 
b = set()
print(type(b))


# Adding value to an empty set 
b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add((4,5,6))
# b.add({4,5}) # Cannot add list or dictionary to sets

# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)


# Lenght of the set
print(len(b)) # Prints the length of this set


# Removal of am items
b.remove(5) # Remove 5 front set b
# b.remove(15) # throws an error while trying to remove 15(which is not present int the set)
print(b)

print(b.pop())
print(b)