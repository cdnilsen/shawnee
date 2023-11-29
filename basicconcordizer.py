from pyuca import Collator

myCollator = Collator()

textSource = open("Voegelin Text.txt", "r", encoding="utf-8")
textLines = textSource.readlines()

allWordDictionary = {}
allShawneeWords = []
currentTextNum = 0
currentLineNum = 0
allWords = []

wordCountDict = {}
for line in textLines:
    line = line.strip()
    lineDict = {}
    lineList = []
    lineSplit = line.split(";")
    if lineSplit[0].strip() == "S":
        for word in lineSplit[1:]:
            if word.strip() not in allWords:
                allWords.append(word.strip())
                wordCountDict[word.strip()] = 1
            else:
                wordCountDict[word.strip()] += 1

allWords.sort(key=myCollator.sort_key)
outputFile = open("Voegelin Concordance.txt", "w", encoding="utf-8")
for word in allWords:
    outputFile.write(word + " (" + str(wordCountDict[word]) + ")\n")
