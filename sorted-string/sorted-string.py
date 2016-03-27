def printString(keys, values):
    stringList = []
    for i in xrange(0, len(keys)):
        for j in xrange(0, values[i]):
            stringList.append(keys[i])
    print "".join(stringList)

T = raw_input("")
T = int(T)

if T < 1 or T > 100:
    exit()

for i in range(0, T):
    S = raw_input("")
    length = len(S)
    if length < 1 or length > 100:
       exit()

    charDictionary = {}
    for c in S:
        if c in charDictionary:
            charDictionary[c] += 1
        else:
            charDictionary[c] = 1

    keys = []
    values = []
    for key,value in charDictionary.items():
        keys.append(key)
        values.append(value)

    for j in xrange(0, len(keys)):
        for k in xrange(j+1, len(keys)):
            if values[j] > values[k]:
                tmp = values[j]
                values[j] = values[k]
                values[k] = tmp

                tmp = keys[j]
                keys[j] = keys[k]
                keys[k] = tmp

            elif values[j] == values[k] and keys[j] > keys[k]:
                tmp = keys[j]
                keys[j] = keys[k]
                keys[k] = tmp
    
    printString(keys, values)