###Cropping words dataBase###
rawBase = open("wordBase/words_alpha.txt", "r")
words = rawBase.readlines()
rawBase.close()

for j in range(5):
    wordLength = j + 5
    strippedWords = []

    for i in words:
        if len(i) == wordLength:
            strippedWords.append(i)

    strippedBase = open("wordBase/stripped_base{}.txt".format(wordLength - 1), "w")
    for i in strippedWords:
        strippedBase.write(i)

    strippedBase.close()
