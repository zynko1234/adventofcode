inputFile = open("input_file", "r")
lines = inputFile.readlines()

entries = []

for entry in lines:
    entries.append(int(entry.replace('\n',"")))

addendA = int()
addendB = int()
addendC = int()
validity = bool()

for i in entries:
    for j in entries:
        for k in entries:
            if i is not j is not k:
                if (i + j + k) == 2020:
                    addendA = i
                    addendB = j
                    addendC = k
                    validity = True
                    break
        
        if validity:
            break
    if validity:
        break

print("{0} + {1} + {2} = {3}".format(i, j, k, (i + j + k)))
print("Answer = {0}".format(i * j * k))