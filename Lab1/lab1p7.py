###
### Problem 7
### Given a list: names = ["Carol", "Albert", "Ben", "Donna"]
### use join() and sorted() to get this output: 
### Albert & Ben & Carol & Donna
names = ["Carol", "Albert", "Ben", "Donna"]

print ("Problem 7 solution follows:")

#The objective is to join this list with '&' and have it in alphabetical order

#Sort alphabetically 
sortedNames = sorted(names)

#Join with '&'
joinedNames = " & ".join(sortedNames)

#Print the names
print(joinedNames)