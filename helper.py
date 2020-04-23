import os 


def findFile():
    x = os.listdir()
    for f in x:
        if(f == "credentials.txt"):
            return True
    return False

result = findFile()
print(result)