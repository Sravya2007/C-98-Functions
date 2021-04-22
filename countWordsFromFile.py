def countWordsFromFile():
    filename = input("Enter the name of file: ")
    numberOfWords = 0
    file = open(filename, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words: ")
    print(numberOfWords)

countWordsFromFile()