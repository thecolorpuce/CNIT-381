bookTitle = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes',
'the', 'great', 'gatsby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

wordCounter = {}

for word in bookTitle:
    if word not in wordCounter:
        wordCounter[word] = 1
    else:
        wordCounter[word] += 1


print(wordCounter)