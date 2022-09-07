#Dictionaries!
#If it's not mentioned, you can also do nested dictionaries, which is pretty rad

elements = {'hydrogen' : 1, 'helium': 2, 'carbon': 6}

"""
Dictionaries can have keys of any immutable type, like integers or tuples, not just strings.
It's not even necessary for every key to have the same type! 
We can look up values or insert new values in the dictionary using square brackets that enclose the key.
"""

print(elements["helium"])   #Prints the value mapped to helium

elements["lithium"] = 3     #Insets lithium with the value of 3 into the dictionary

for k, v in elements.items():
    print(f"{k.title()}: {v}")
    print("\n")


"""
We can check whether a value is in a dictionary the same way we check whether a value is in a list or set with the in keyword.
Dicts have a related method that's also useful, get. get looks up values in a dictionary, but unlike square brackets, 
get returns None (or a default value of your choice) if the key isn't found.
"""

print("carbon" in elements)         #checks to see if carbon is in the dict
print(elements.get("carbon"))       #Prints the value associated with carbon (6)

print(elements.get("dilithium"))    #Does not exist in the list, retruns "None"