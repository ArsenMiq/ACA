def findUAM(logs, k):
    mapDict = {}
    for i in range(len(logs)):
        if logs[i][0] in mapDict:
            if logs[i][1] in mapDict[logs[i][0]]:
                continue
            else:
                mapDict[logs[i][0]].append(logs[i][1])
        else:
            mapDict[logs[i][0]] = [logs[i][1]]
    
    result = [0 for i in range(k)]

    for i in mapDict:
        result[len(mapDict[i]) - 1] += 1
    return result
        
logs = [[1,1],[2,2],[2,3]]
k = int(input("Type k : "))

print(findUAM(logs, k))
