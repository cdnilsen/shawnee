# turns glossed lines from the output into more readable files in the /texts/ folder

import os

def getLineDict(rawLine):
    rawDict = {}
    splitLetter = "Ĝ"
    isShawnee = ("Ŝ" in rawLine)
    if isShawnee:
        splitLetter = "Ŝ"
    rawDict["isShawnee"] = isShawnee
    
    splitLine = rawLine.split(splitLetter)

    rawDict["address"] = splitLine[0].split(".")[1]
    rawDict["text"] = splitLine[1].strip()

    return rawDict

def getRightTextLines(lines, textNum):
    allLines = []
    for line in lines:
        if ("." in line):
            splitLine = line.split(".")[0]
            if int(splitLine) == textNum:
                lineDict = getLineDict(line)
                allLines.append(lineDict)
    
    textDict = {}
    addressCount = 0
    for lineDict in allLines:
        address = lineDict["address"]        
        isShawnee = lineDict["isShawnee"]
        text = lineDict["text"]
     
        if address not in textDict:
            textDict[address] = {}
            textDict[address]["Shawnee"] = ""
            textDict[address]["Gloss"] = ""
        if isShawnee:
            textDict[address]["Shawnee"] = text
        else:
            textDict[address]["Gloss"] = text
        
        if int(address) > addressCount:
            addressCount = int(address)
      
    textDict["numLines"] = addressCount 
    return textDict
        

def splitText(line, splittingChar):
    return line.strip().split(splittingChar)

def compareShawneeAndGloss(shawneeText, gloss):
    return (len(splitText(shawneeText, " ")) == len(splitText(gloss, "|")))


def processShawnee(word):

    punctuation = [".", '"', "'", ",", "?", "!", "“", "”"]

    for char in punctuation:
        word = word.replace(char, " ")
    
    return word.lower()

#print(processShawnee("Yʔkweewa,"))

def processEnglish(gloss):

    return gloss

def processIntoNewFile(textNum, lineDict):
    fileName = './texts/' + str(textNum) + '.txt'
    newFile = open(fileName, 'w', encoding='utf-8')
    numLines = lineDict["numLines"]

    print(numLines)
    for i in range(1, numLines+1):
        newFile.write("==" + str(i) + "==\n")
        shawneeText = lineDict[str(i)]["Shawnee"]
        glossText = lineDict[str(i)]["Gloss"]

       
        splitShawnee = splitText(shawneeText, " ")
        splitGloss = splitText(glossText, "|")

        for j in range(len(splitShawnee)):
            line = processShawnee(splitShawnee[j]) + " \\\\ " + splitGloss[j] + "\n"
            newFile.write(line) 


def processText():
    rawLines = open("./output.txt", "r", encoding="utf8").readlines()
    textNum = int(input("Process text #: "))

    dict = getRightTextLines(rawLines, textNum)

    numLines = dict["numLines"]

    if numLines == 0:
        print("\nText #" + str(textNum) + " not found in output.txt")
    else:
        print("\nProcessing text #" + str(textNum))
        print("(" + str(numLines) + " lines)")


    allGlossesMatch = True
    for i in range(1, numLines+1):
        shawneeText = dict[str(i)]["Shawnee"]
        gloss = dict[str(i)]["Gloss"]


        if (compareShawneeAndGloss(shawneeText, gloss) == False):
            print("Number of glosses don't match at line " + str(i))
            allGlossesMatch = False
    
    if allGlossesMatch:
        processIntoNewFile(textNum, dict)



        #print(shawneeText)
        #print(gloss)
    #print(matchingLines)


def getWordlist(startText, endText):
    splitter = "\\\\"
    allWords = []
    glossDict = {}
    addressDict = {}
    for i in range(startText, endText + 1):
        filePath = "./texts/" + str(i) + ".txt"
        if not os.path.isfile(filePath):
            continue

        file = open(filePath, "r", encoding="utf-8")
        fileLines = file.readlines()
        currentSentence = 1
        for line in fileLines:
            if splitter in line:
                splitLine = line.split(splitter)
                shawnee = splitLine[0].strip()
                gloss = splitLine[0].strip()
                address = str(i) + "." + str(currentSentence)
                if processShawnee(shawnee) not in allWords:
                    #glossDict[shawnee] = [gloss]
                    #addressDict[shawnee] = [address]
                    allWords.append(processShawnee(shawnee))
            elif line.strip().startswith('==') and line.strip().endswith('=='):
                num = line.replace("=", "")
                try:
                    currentSentence = int(num)
                except:
                    print(i)
                    print(line)
        file.close()

    
    outputFile = open("./texts/wordlist.txt", "w", encoding="utf-8")
    allWords.sort()
    for word in allWords:
        outputFile.write(word + "\n")
    #print("Printing wordlist...")

def main():
    doWhat = input("Do you want to process a text (1) or get a wordlist (2)? ").strip()

    if doWhat == "1":
        processText()
    elif doWhat == "2":
        startText = input("Get a list from text #: ").strip()
        endText = input("To text #: ").strip()

        if (startText.isnumeric() and endText.isnumeric):
            if int(endText) >= int(startText):
                getWordlist(int(startText), int(endText))
            else:
                print("\n")
                main()
        else:
            print("\n")
            main()
    else:
        main()


#main()


def getTextNum(line):
    line = line.strip()
    if line != "" and "." in line:
        return int(line.split(".")[0])
    else:
        return 0

def listTranscripts(existingCopies):
    rawLines = open("./output.txt", "r", encoding="utf8").readlines()

    allTextNums = []
    for i in range (1, 219):
        allTextNums.append(str(i))

    textExistsDict = {}
    for textNum in allTextNums:
        textExistsDict[textNum] = False

    for line in rawLines:
        lineTextNum = getTextNum(line)
        if lineTextNum != 0:
            textExistsDict[str(lineTextNum)] = True


    listOfTexts = []
    for textNum in allTextNums:
        if (existingCopies == textExistsDict[textNum]):
            listOfTexts.append(textNum)

    print(listOfTexts)
    print(str(len(listOfTexts)) + " texts total")
    

listTranscripts(False)
#main()
    