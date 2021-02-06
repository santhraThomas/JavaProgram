"""
string1 = input("please enter some words: ")
listOfWords = string1.split()
wordLength = len(listOfWords)
print(wordLength)
print(string1)
"""
fName = open("openfolder.txt", "r")
for line in fName:
    print(line)
    posOfDash = line.find('-')
    print(posOfDash)
#listOfWords = string.split()
#wordLength = len(listOfWords)
#print(wordLength)
#print(string1)
