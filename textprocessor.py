lastTexts = open('Voegelin Text 190-218.txt', 'r', encoding="utf-8")

textLines = lastTexts.readlines()


currentText = 0
currentLine = 0

currentSplitShawnee = []
currentSplitGlosses = []

outputFile = open('voegein190-218.txt', 'w', encoding="utf-8")
for line in textLines:
    splitLine = line.strip().split()
    if len(splitLine) > 0:
        if splitLine[-1].strip() == "{":
            currentText = int(splitLine[0])
        elif splitLine[-1].strip() == "[":
            currentLine = int(splitLine[0])
        else:
            if splitLine[0] == "Ŝ":
                newSplit = line.strip().split(';')
                currentSplitShawnee = newSplit
            elif splitLine[0] == "Ĝ":
                newSplit = line.strip().split(';')
                currentSplitGlosses = newSplit

                newLine = str(currentText) + "." + str(currentLine) + ".Ŝ " + " ".join(currentSplitShawnee[1:]) + "\n" +  str(currentText) + "." + str(currentLine) + ".Ĝ " + "|".join(currentSplitGlosses[1:]) + "\n\n"
                outputFile.write(newLine)
                if len(currentSplitShawnee) == len(currentSplitGlosses):
                    continue
                    #for i in range(len(currentSplitShawnee)):
                        #print(currentText, currentLine, currentSplitShawnee[i], currentSplitGlosses[i])
                else:
                    print("ERROR: Different lengths of Shawnee and Glosses at line", currentText, currentLine)