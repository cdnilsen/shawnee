from pyuca import Collator

myCollator = Collator()

textSource = open("output.txt", "r", encoding="utf-8")
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
    if len(line) > 0:
        lineSplit = line.split(" ")
        if lineSplit[0].strip()[-1] == "Ŝ":
            for word in lineSplit[1:]:
                newWord = word.strip()
                newWord = newWord.lower()
                newWord = newWord.replace('“', "")
                newWord = newWord.replace('”', "")
                newWord = newWord.replace('"', "")
                newWord = newWord.replace(',', "")
                newWord = newWord.replace('.', "")
                newWord = newWord.replace('!', "")
                newWord = newWord.replace('?', "")
                newWord = newWord.replace(':', "")
                newWord = newWord.replace(';', "")
                if newWord not in allWords:
                    allWords.append(newWord)
                    wordCountDict[newWord] = 1
                else:
                    wordCountDict[newWord] += 1

allWords.sort(key=myCollator.sort_key)
outputFile = open("Voegelin Concordance.txt", "w", encoding="utf-8")
for word in allWords:
    outputFile.write(word + " (" + str(wordCountDict[word]) + ")\n")
