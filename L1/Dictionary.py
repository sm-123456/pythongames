#Dictionary is collection of items in pairs called key-value pair

MyDict={
    "Tanshi":"Black",
    "Satwik":"Blue",
    "Sam":"Green",
    "Austin":"Orange",
    "Diya":"White"
}
print(MyDict)

#print only keys
print(MyDict.keys())
# print only values
print(MyDict.values())

#only print Satwik's color
print(MyDict["Satwik"])
MyDict["Satwik"]="navy"
print(MyDict["Satwik"])
MyDict.update({"Satwik":"SkyBlue"})
print(MyDict["Satwik"])