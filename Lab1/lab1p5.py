###
### Problem 5
### Select the three most recent dates from this list using list slicing notation.
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
'March 9, 2016']

print ("Problem 5 solution follows:")

#The three most recent dates
#Nice that they're in order

recent_dates = eclipse_dates[-3 : None] #starting at index -3 (3rd from last) and ending with 'None' as index -1 will ber Mar 20, 2015

print(eclipse_dates)
print("The 3 most recent days are as follows:")
for e in recent_dates:
    print(f"\t{e}")