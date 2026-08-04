myDict={}

engS=int(input("Enter Your English Score: "))
myDict.update({"English":engS})

mathS=int(input("Enter Your Maths Score: "))
myDict.update({"Maths":mathS})

bioS=int(input("Enter Your Biology Score: "))
myDict.update({"Biology":bioS})

chemS=int(input("Enter Your Chemistry Score: "))
myDict.update({"Chemistry":chemS})

phyS=int(input("Enter Your Physics Score: "))
myDict.update({"Physics":phyS})

print(myDict)

average=(engS+mathS+bioS+chemS+phyS)/5

print(f"Your average score is {average}")