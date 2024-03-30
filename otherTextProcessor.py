import os

textFile = './machinetexts/'



output = open('output.txt', 'w', encoding="utf-8")
for i in range(4, 150):
    filename = f"{textFile}{i}.txt"
    if os.path.exists(filename):
        fileLines = open(filename, 'r', encoding="utf-8")
        lineCounter = 1
        shawneeLines = []
        glossLines = []
        for line in fileLines:
            if line[0] == "Ŝ":
                shawneeLine = str(i) + "." + str(lineCounter) + ".Ŝ " + line[2:]
                shawneeLines.append(shawneeLine)
            elif line[0] == "Ĝ":
                glossLine = str(i) + "." + str(lineCounter) + ".Ĝ " + line[2:]
                glossLines.append(glossLine)
                lineCounter += 1
            else:
                continue
        if (len(shawneeLines) == len(glossLines)):
            for j in range(len(shawneeLines)):
                output.write(shawneeLines[j])
                output.write(glossLines[j])
                output.write("\n\n")                 
        else:
            print("ERROR: Different lengths of Shawnee and Glosses at line", i, j)
    else:
        continue