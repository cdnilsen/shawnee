from pyuca import Collator

myCollator = Collator()

onlyShawnee = open("Shawnee Only.txt", "r", encoding="utf-8")

shawneeLines = onlyShawnee.readlines()

allWords = []

outputConcordance = open("voegelinConcordance.txt", "w", encoding="utf-8")
verseDict = {}
totalWordCountDict = {}
wordVerseDict = {}

for line in shawneeLines:
    line = line.strip()
    lineDict = {}
    wordList = []
    lineSplit = line.split(" ")
    citePlace = lineSplit[0]
    verseDict[citePlace] = []
    for word in lineSplit[1:]:
        if word not in lineDict:
            wordList.append(word)
            lineDict[word] = 1
        else:
            lineDict[word] += 1

    verseDict[citePlace] = []
    
    wordList = sorted(wordList, key=myCollator.sort_key)

    for word in wordList:
        verseDict[citePlace].append((word, lineDict[word]))
        if word not in totalWordCountDict:
            allWords.append(word)
            totalWordCountDict[word] = lineDict[word]
            wordVerseDict[word] = [(citePlace, lineDict[word])]
        else:
            totalWordCountDict[word] += lineDict[word]
            wordVerseDict[word].append((citePlace, lineDict[word]))
    
sortedWords = sorted(allWords, key=myCollator.sort_key)

for word in sortedWords:
    totalCount = totalWordCountDict[word]

    if totalCount == 1:
        stringCount = ""
    else:
        stringCount = " (" + str(totalCount) + ")"

    finalString = word + stringCount + ": "

    for tuple in wordVerseDict[word]:
        if tuple[1] == 1:
            finalString += tuple[0] + ", "
        else:
            finalString += tuple[0] + " (" + str(tuple[1]) + "), "
    
    finalString = finalString[:-2]
        
    
    outputConcordance.write(finalString + "\n")


# Produces text lines for the main notebook copy. Turn off if not needed
produceTextLines = False

textNum = [137]
numSentences = [5] 
if produceTextLines:
    for i in range(len(textNum)):
        outputConcordance.write(str(textNum[i]) + ":\n")
        for j in range (1, numSentences[i] + 1):
            outputConcordance.write(str(textNum[i]) + "." + str(j) + ".S:\n")
            outputConcordance.write(str(textNum[i]) + "." + str(j) + ".G:\n")
            outputConcordance.write(str(textNum[i]) + "." + str(j) + ".E:\n\n")


