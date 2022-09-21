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

def sortedMerge(a, b):
    """Sorted Merge
    We're trying to numerically sort two lists
    
    INPUT:
    Two equal length lists of numerics
    
    OUTPUT:
    The contents of the two lists merged into one list, and sorted numerically"""
    index = -1
    
    #Insert the contents of b into a
    for i in range(5):
        if a[index] > b[index]:
            for j in a:
                if b[index] > j:
                    a.insert(index, b[index])
            #a.insert(index, b[index])
            #index -= 1
        elif a[index] < b[index]:
            a.insert(index, a[index])
            index -= 1
        else:
            break




    
    #Find a method to sort the contents withoug sort()


sortedMerge(A, B)       #Call the function, and print
print(A)
