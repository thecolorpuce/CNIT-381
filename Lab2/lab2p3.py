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
print ("Problem 3 solution follows:")

def lucky_int(list):
    """Lucky int... Number appears the same number of times as its value. 2 would be lucky if it showed up twice.
        INPUT:
        A list of integers
        
        OUTPUT:
        Lucky Integers"""

#I guess I could do something weird

    c1 = 0
    c2 = 0
    lucky = {}

    for i in list:
        if i not in lucky:
            lucky[i] = 1
        else:
            lucky[i] += 1
    print(lucky)
    for i, v in lucky.items():
        if(i == v):
            return i
        else:
            return -1
    return lucky






print(f"\n{lucky_int(nums1)}")
print(f"\n{lucky_int(nums2)}")
print(f"\n{lucky_int(nums3)}")