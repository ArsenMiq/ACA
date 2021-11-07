def getNumPattern(word):
    words = list(word)
    replace = {}
    index = 0
    result = ''
    for i in range(len(words)):
        if words[i] in replace:
            result = result + str(replace.get(word[i]))
        else:
            replace[words[i]] = index
            index += 1
            result = result + str(index)
            
        result = result + str(index)

    return result

def findPatterns(words, pattern):
    patternNum = getNumPattern(pattern)
    pats = []
    for i in range(len(words)):

        if patternNum == getNumPattern(words[i]):
            pats.append(words[i])

    return pats


words = []
words = [i for i in input("words = ").split()]
pattern = input("type a pattern : ")
print(findPatterns(words, pattern))
