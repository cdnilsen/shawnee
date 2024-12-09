import os

alfordList = open('../alfordWordsPlain.txt', 'r', encoding='utf-8').readlines()

def processAlfordWord(line):
    replacementDict = {
        "c": "č",
        "s": "š",
        "f": "θ"
    }

    keys = ["c", "s", "f"]

    alfordWord = line.split("(")[0].strip()
    
    for key in keys:
        alfordWord = alfordWord.replace(key, replacementDict[key])

    consonants = ["p", "t", "č", "k", "m", "n", "θ", "š", "h", "w", "y", "l"]

    for consonant in consonants:
        hC = "h" + consonant
        glottalC = "ʔ" + consonant
        alfordWord = alfordWord.replace(hC, glottalC)

    return alfordWord

allAlfordLinesList = []

for line in alfordList:
    allAlfordLinesList.append(processAlfordWord(line))

def processTextLine(line, dict):
    if "\\\\" in line:
        word = line.split("\\\\")[0].strip()
        spuriousChars = ["[", "]", "(", ")", "{", "}", "<", "="]
        for char in spuriousChars:
            word = word.replace(char, "")
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
        return True
    else:
        return False

def getAllTextFiles():
    masterDict = {}
    textFileHandle = "../texts"
    allWordCount = 0
    for entry in os.listdir(textFileHandle):
        subFolder= textFileHandle + "/" + entry
        for entry in os.listdir(subFolder):
            fileLines = open(subFolder + "/" + entry, "r", encoding="utf-8").readlines()
            for line in fileLines:
                if processTextLine(line, masterDict):
                    allWordCount += 1

    allWords = list(masterDict.keys())

    hapaxCount = 0
    disCount = 0
    trisCount = 0
    for word in allWords:
        if masterDict[word] == 1:
            hapaxCount += 1
        elif masterDict[word] == 2:
            disCount +=1
        elif masterDict[word] == 3:
            trisCount += 1

    print(str(hapaxCount) + " hapaxes")
    print(str(disCount) + " dis legomena")
    print(str(trisCount) + " tris legomena\n")
    print(str(len(allWords)) + " total words")
    print(str(allWordCount) + " total tokens")

getAllTextFiles()