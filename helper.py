import os 


def findFile():
    x = os.listdir()
    for f in x:
        if(f == "credentials.txt"):
            return True
    return False



def email(emailormessage, senderEmailaddr, password, reciever):
    files = open("credentials.txt", "w")
    files.write(f"{emailormessage}" + "\n")
    files.write(f"{senderEmailaddr}" + "\n")
    files.write(f"{password}" + "\n")
    files.write(f"{reciever}")
    files.close()


def text(emailormessage, twilionumber, twiliosid, twiliotoken, reciever):
    files = open("credentials.txt", "w")
    files.write(f"{emailormessage}" + "\n")
    files.write(f"{twilionumber}" + "\n")
    files.write(f"{twiliosid}" + "\n")
    files.write(f"{twiliotoken}" + "\n")
    files.write(f"{reciever}")
    files.close()



