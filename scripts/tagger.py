# ONLY USE ON PROOFED TEXTS.

def canTag(initialLine):
    return initialLine.strip() == "<PROOFED>"

def tagWord(lineDict, headword, isMarginal, mandatoryGloss = ""):
    word = lineDict["word"]
    gloss = lineDict["gloss"]

def processLine(line, headword, mandatoryGloss = ""):
    finalString = ""
    if "\\\\" in line:
        splitLine = line.split("\\\\")
        if len(splitLine) == 2:
            isMarginal = (line[0] == "<" and line[-1] == ">")
            if isMarginal:
                line = line.replace("<", "").replace(">", "")
            lineDict = {}
            lineDict["word"] = splitLine[0].strip()
            lineDict["gloss"] = splitLine[1].strip()
            tagWord(lineDict, headword, isMarginal, mandatoryGloss)

        else:
            finalString = line


