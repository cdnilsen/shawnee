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
