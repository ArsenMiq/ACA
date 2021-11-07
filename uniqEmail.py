def addPoint(email):
    domain = email.split("@", 1)[1]
    name = email.split("@", 1)[0]
    subDomain = domain.split('.', 1)[0]
    index = len(subDomain)
    domain = domain[:index // 2]+ '.' + domain[index // 2:]
    return name + '@' + domain

def convertToOrigin(email):
    name = email.split("@",1)[0]
    name = name.split("+",1)[0] 
    name = name.replace('.', '')
    domain = email.split("@",1)[1]
    return name + '@' + domain

def numUniqEmails(emails):
    origins = []
    for i in range(len(emails)):
        originEmail = convertToOrigin(emails[i])
        if originEmail in origins:
            origins.append(addPoint(originEmail))
        else:
            origins.append(originEmail)

    return origins


emails = []
emails = [i for i in input("Type emails : ").split()]
forward = numUniqEmails(emails)
print(forward)
print(len(forward))
