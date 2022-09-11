###
### Problem 1 (20 points)
### Is Unique: Implement an algorithm to determine if a string has all unique characters. 
### Sample Output:
### "abcdefg" is Unique 
### "abcdebg" is not

print ("Problem 1 solution follows:")
input = input("Input a string: ")# Takes a string as an input

#I think I could itterate through the string, and make a counter for each character in the string

def unique(string):
    #I'm stupid. The best method I can figure is to make use of two for loops
    #loop 'v' steps into a second for loop 'j'
    #Essentially we start at the first position with the first for loop.
    #Then we loop through the string
    #If the same value is found, we return false
    #If no values are foun, we return True
    for i in range(0, len(string)):
        for j in range(i + 1, len(string)):
            if(string[i] == string[j]):
                return "This string is not Unique"            #Return Flase if v&j match
    return "This string is unique"                        #Retrun True if loop completes


print(unique(input))    #Call the function, and go forth.
