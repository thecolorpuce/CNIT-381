###
### Problem 5 (30 points)
### Sorted Merge: You are given two sorted integer lists, A and B, where A has a large enough 
### buffer at the end to hold B. Write a function to merge B into A in sorted order.
###
### Example:
### A = [1,3,4,8,9]
### B = [2,4,5,6,7]
### output [1,2,3,4,4,5,6,7,8,9]

print ("Problem 5 solution follows:")

#A sorted buffer. I think we could make use of the zip function for this
#I'll make use of the two provided lists above

A = [1,3,4,8,9]
B = [2,4,5,6,7]
C = []                      #Created an empty list to use

def sortedMerge(a, b):
    """Sorted Merge
    We're trying to numerically sort two lists
    
    INPUT:
    Two equal length lists of numerics
    
    OUTPUT:
    The contents of the two lists merged into one list, and sorted numerically"""
    h = []                  #Empty list for the function
    
    for i, j in zip(a, b):  #Making use of zip. i for A, j for B
        output = i          #Assigning the output of i to "output" (I do the same thing with j)
        h.append(output)    #Appends the outputs to the h list
        output = j
        h.append(output)
        
    h.sort()                #Sorted the list in numerical order
    return h
C = sortedMerge(A, B)       #Call the function, and print

print(C)


#I just noticed that I missed the point of this. I'm supposed to merge B into A. Not create a brand new list...
#I'll still keep this around though