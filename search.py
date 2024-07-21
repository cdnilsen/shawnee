import os

def openText(filePath, i, dict):
    file = open(filePath, "r", encoding="utf-8")

    lines = file.readlines()

    for line in lines:
        if "\\\\" in line:
            splitLine = line.split("\\\\")
            shawnee = splitLine[0]
            gloss = splitLine[1]
            if shawnee not in dict:
                dict[shawnee] = {}
                dict[shawnee][str(i)] = {gloss: 1}
            elif str(i) not in dict[shawnee]:
                dict[shawnee][str(i)] = {gloss: 1}
            elif gloss not in dict[shawnee][str(i)]:
                dict[shawnee][str(i)][gloss] = 1
            else:
                dict[shawnee][str(i)][gloss] += 1


def getAllTexts():
    dict = {}
    for i in range(1, 219):
        filePath = "./texts/" + str(i) + ".txt"
        if os.path.isfile(filePath):
            openText(filePath, i, dict)
    return dict


def cleanShawneeWord(word):
    for char in "[](){}=-":
        word = word.replace(char, "")
    return word.strip()

def searchShawnee():
    print("Use <q> for <ʔ> and <f> for <θ>")
    searchString = input("String: ").strip()

    searchString = searchString.replace("q", "ʔ")
    searchString = searchString.replace("f", "θ")
    dict = getAllTexts()

    allShawneeWords = list(dict.keys())

    matchingWords = []

    for word in allShawneeWords:
        if searchString in cleanShawneeWord(word):
            matchingWords.append(word)

    finalString = str(len(matchingWords)) + " found: "

    matchingWords.sort()
    for word in matchingWords:
        finalString += word.strip() + ", "

        print(word.strip() + ":")
        allGlosses = ""
        for text in dict[word]:
            for gloss in dict[word][text]:
                allGlosses += "\t" + gloss.strip() + "\n"

        print(allGlosses[0:-1])
    print(finalString[0:-2])

    print(str(len(matchingWords)) + " words found")

def searchEnglish():
    searchString = input("String: ")
    dict = getAllTexts()
    allShawneeWords = list(dict.keys())

    allWords = []
    wordToGlossDict = {}
    wordToTextDict = {}

    for word in allShawneeWords:
        appears = False
        allGlosses = []
        glossDict = {}
        allTexts = list(dict[word].keys())
        for text in allTexts:
            allGlosses = list(dict[word][text].keys())
            for gloss in allGlosses:
                if searchString in gloss:
                    appears = True
                    print(text)
                    if gloss not in glossDict:
                        allGlosses.append(gloss)
                        glossDict[gloss] = [text + ":" + str(dict[word][text][gloss])]
                    else:
                        glossDict[gloss].append(text + ":" + str(dict[word][text][gloss]))
        if appears:
            allWords.append(word)
            wordToGlossDict[word] = allGlosses
            wordToTextDict[word] = glossDict

    totalCount = 0
    for word in allWords:
        outputText = word.strip() + ":\n"
        thisWordGlosses = []
        for gloss in wordToGlossDict[word]:
            if gloss not in thisWordGlosses:
                outputText += gloss
            thisWordGlosses.append(gloss)
        totalCount += 1

        print(outputText)

    finalString = str(totalCount) + " words found: "

    allWords.sort()
    for word in allWords:
        finalString += word.strip() + ", "
    print(finalString[0:-2])
    

def main():
    doWhat = input("Search for a Shawnee word (1) or an English gloss (2): ")
    if doWhat != "1" and doWhat != "2":
        main()
    else:
        if doWhat == "1":
            searchShawnee()
        else:
            searchEnglish()

main()
