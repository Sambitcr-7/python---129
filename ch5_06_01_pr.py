myDict ={
    "Pankha": "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi World\n")
# print("The meaning of your world is :" < myDict[a])

# Below line will not throw an error if the key is not present in the dictionary

print("The meaning of your world is:", myDict.get(a))