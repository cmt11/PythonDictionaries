def createDictionary(myList):
    dictionary = dict()
    i = 0
    while i < len(myList):
        dictionary[i] = myList[i]
        i+=1
    return dictionary


def histogram(word):
    dictionary = dict()
    for letter in word:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary


def alphabeticalHistogram(word):
    dictionary = histogram(word)
    myList = []
    for key in dictionary:
        myList.append(key)
    i = 0
    while i < len(myList)-1:
        while i < len(myList)-1:
            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
            i+=1
        i+=1
    x = 0
    while x < len(myList):
        print myList[x], dictionary[myList[x]]
        x+=1


def reverseLookup(dictionary, value):
    i = 0
    while i < len(dictionary):
        if dictionary[i] == value:
            return i
        i+=1
