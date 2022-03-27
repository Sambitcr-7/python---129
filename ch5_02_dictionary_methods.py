


myDict = {
    "fast": "In a Quick Manner",
    "harry": "An Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'harry':'player'},
    1:2
}
# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.value()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (keys,value) for all contents of the dictionary
print(myDict)
updateDict = {
    "Lovish" : "Friend",
    "sam"    : "Friend",
    "shubham" : "Friend",
    "harry"  :  "A Dancer"
}
myDict.update(updateDict) #Updates the dictionary  by adding with key-value pairs from updateDict
print(myDict)

print(myDict.get("harry2")) # Returns none  as harry2 is not present in the dictionary
print(myDict["harry2"]) # throws an error as.harry2.is.not.present.in.the.dictionary

# The difference between .get and [] systex in Dictionaries?
print(myDict.get("harry2")) # Returns none  as harry2 is not present in the dictionary
print(myDict["harry2"]) # throws an error as.harry2.is.not.present.in.the.dictionary