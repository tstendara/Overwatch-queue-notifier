import os 


def findFile():
    x = os.listdir()
    for f in x:
        print(f)
        if(f == "credentials.txt"):
            return True
    return False

