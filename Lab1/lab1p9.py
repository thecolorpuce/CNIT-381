###
### Problem 9
### Define a Dictionary, population,that provides information on 
### the world's largest cities and print it out. The key is the name of a city
### a string), and the associated value is its population in
### millions of people.
###   Key     |   Value
### Shanghai  |   17.8
### Istanbul  |   13.3
### Karachi   |   13.0
### Mumbai    |   12.5

print ("Problem 9 solution follows:")

#Create the dictionary. Using provided examples...

cities = {'Shanghai': 17.8,
        'Istanbul': 13.3,
        'Kerachi': 13.0,
        'Mumbai': 12.5,
        }

#Use a for loop to itterate through the dictionary, and print the key & value.

for k, v in cities.items(): #Using the items method for keys and values
    print(f"City: {k.title()} || Population: {v} million.")