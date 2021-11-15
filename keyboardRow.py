def getWords(word):
    letters = [["qwertyuiop"],
        ["asdfghjkl"],
        ["zxcvbnm"]]

    arr = list(word)
    isContain = False
    result = ''
    for i in range(len(letters)):
        s = str(letters[i])
        s_upper = s.upper()
        for j in range(len(arr)):
            let = arr[j]
            if let in s or let in s_upper:
                isContain = True
                result += let
        if isContain:
            break

    return result

def getWordsContain(words):
    result = []
    for i in range(len(words)):
        if getWords(words[i]) == words[i]:
            result.append(words[i])

    return result


words = ["Hello", "Alaska", "Dad", "Pease"]
print(getWordsContain(words))
words = ["omk"]
print(getWordsContain(words))
words = ["adsdf", "sdf"]
print(getWordsContain(words))
