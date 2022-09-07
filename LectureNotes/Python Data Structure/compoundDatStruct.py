"""
We can include containers in other containers to create compound data structures. 
For example, this dictionary maps keys to values that are also dictionaries!
"""

elements = {"hydrogen": {"number": 1,
                        "wight": 1.00794,
                        "symbol": "H"},
            "helium":   {"number": 2,
                        "weight": 4.002602,
                        "symbol": "He"}}

helium = elements["helium"] #Get the helium dictionary

#hydrogen_weight = elements["hydrogen"]['weight']    #Get the weight of hydrogen

oxygen = {"number": 8, "weight": 15.999, "symbol": "O"}     #Create a new oxygen dictionary

elements["oxygen"] = oxygen     #Assign 'oxygen' as a key to the elements dictionary

print('elements = ', elements)