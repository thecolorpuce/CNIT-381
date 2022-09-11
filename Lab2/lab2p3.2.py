###
### Problem 3 (10 points)
### Given a list of integers, a lucky integer is an integer which has a frequency 
### in the list equal to its value.
### Return a lucky integer in the list. If there is no lucky integer return -1.
###
### Example 1:
### Input: [2,2,3,4]
### Output: 2
### Explanation: The only lucky number in the list is 2 because frequency[2] == 2.
###
### Example 2:
### Input: [1,2,2,3,3,3]
### Output: 3
### Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
###
### Example 3:
### Input: [2,2,2,3,3]
### Output: -1
### Explanation: There are no lucky numbers in the list.


nums1 = [2,2,3,4,4]
nums2 = [1,2,2,3,3,3]
nums3 = [2,2,2,3,3]
nums4 = [1,3,3,2,6,2]
print ("Problem 3 solution follows:")

def lucky_int(list):
    """Lucky int... Number appears the same number of times as its value. 2 would be lucky if it showed up twice.
        INPUT:
        A list of integers
        
        OUTPUT:
        Lucky Integers"""

#I guess I could do something weird

    c1 = 0
    lucky = {}                   #A dictionary that I use to store the key(value from list) and value(number of times the value appears in the list)
    list.sort()                  #Not relevant in this example, but this will ensure unsorted lists will bring back the largest value

    #I should make a dictionary that holds the key(list) and value (number of times integer appears in the list)
    for i in list:              #A for loop that itterates through the provided list
        if i not in lucky:      #if the integer is not in the 'lucky' dictionary, we add it, and assign it a value of 1
            lucky[i] = 1
        else:
            lucky[i] += 1       #If the value already exists, we increment the value of the integer by 1. If we have two 2's, the key value pair would be {2: 2}

    #The dictionary 'lucky' now has associated values. 
    #Ittereate through the dictionary, and find the largest value that is lucky
    for k, v in lucky.items():  #for loop itterating through the dictionary. k(key), v(value)
        if k == v:              #If the key == the value, we assign the variable c1 to = k
            c1 = k              #this is overwritten when a new value enters the scope. Since this is sorted, that value will be larger
        else:
            continue            #If k != v, we continue looping
    
    if c1 == 0:                 #Requirements wanted to return a -1 instead of a 0
        return -1
    return c1



#This is close. I'll come back to it in a bit


print(f"\n{lucky_int(nums1)}")
print(f"\n{lucky_int(nums2)}")
print(f"\n{lucky_int(nums3)}")
print(f"\n{lucky_int(nums4)}")  #My extra example list nums4 working as intended