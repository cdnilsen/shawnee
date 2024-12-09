import os

masterDict = {}
textFileHandle = "../texts"

# mode can be 'starts with' (s), 'ends with' (e) or 'contains' (c)
def grabWords(dict, string, mode):
    wordList = list(dict.keys())

    finalList = []
    if mode == 'b':
        for word in wordList:
            if word.startswith(string):
                finalList.append(word)
    elif mode == 'e':
        for word in wordList:
            if word.endswith(string):
                finalList.append(word)
    elif mode == 'c':
        for word in wordList:
            if string in word:
                finalList.append(word)
    
    return finalList

def getWordCount(word, dict):
    totalCount = 0
    allTextIDs = dict[word]
    idList = []
    for id in allTextIDs:
        idList.append(id)
        thisTextCount = dict[word][id]
        totalCount += thisTextCount

    finalDict = {
        'texts': idList,
        'count': totalCount
    }

    return finalDict

def getWord(line, dict, entry):
    textID = entry.replace(".txt", "")
    word = line.split("\\\\")[0].strip()
    spuriousChars = ["[", "]", "(", ")", "{", "}", "<", "="]
    for char in spuriousChars:
        word = word.replace(char, "")
    
    if word in dict:
        if textID in dict[word]:
            dict[word][textID] += 1
        else:
            dict[word][textID] = 1
    else:
        dict[word] = {}
        dict[word][textID] = 1

def getDict():

    dict = {}
    textFileHandle = "../texts"
    for entry in os.listdir(textFileHandle):
        subFolder= textFileHandle + "/" + entry
        for entry in os.listdir(subFolder):
            fileLines = open(subFolder + "/" + entry, "r", encoding="utf-8").readlines()
            for line in fileLines:
                if "\\\\" in line:
                    getWord(line, dict, entry)

    return dict

def runSearch():
    dict = getDict()

    typedMode = input("Look for Shawnee words that begin (b) or end (e) with a string? Anything else will just look at words that contain it. Use <?> after a character to make it optional (not yet implemented) ").strip()

    mode = 'c'
    if typedMode == 'b' or typedMode == 'e':
        mode = typedMode

    string = input("Search for a string. Use <f> for /θ/, <q> for /ʔ/, and <c s> for /č š/. ").strip()

    replaceDict = {
        "f": "θ",
        "q": "ʔ",
        "c": "č",
        "s": "š"
    }

    for char in ["f", "q", "c", "s"]:
        string = string.replace(char, replaceDict[char])

    finalList = []
    if string != "":
        finalList = grabWords(dict, string, mode)

    totalCount = 0
    for word in finalList:
        wordCountDict = getWordCount(word, dict)
        count = wordCountDict['count']
        textList = wordCountDict['texts']

        textListString = '['
        for id in textList:
            textListString += str(id) + ", "
        textListString = textListString[0:-2] + "]"

        string = word + " (" + str(count) + ") " + textListString
        totalCount += count
        print(string)

    print(str(len(finalList)) + " words found")
    print(str(totalCount) + " tokens total")

runSearch()