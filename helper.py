import os 
import requests

def findFile():
    x = os.listdir()
    for f in x:
        if(f == "credentials.txt"):
            return True
    return False


def email(emailormessage, reciever):
    os.system("echo test > credentials.txt")
    files = open("credentials.txt", "w")
    files.write(f"{emailormessage}" + "\n")
    files.write(f"{reciever}")
    files.close()


def text(emailormessage, twilionumber, twiliosid, twiliotoken, reciever):
    os.system("echo test > credentials.txt")
    files = open("credentials.txt", "w")
    files.write(f"{emailormessage}" + "\n")
    files.write(f"{twilionumber}" + "\n")
    files.write(f"{twiliosid}" + "\n")
    files.write(f"{twiliotoken}" + "\n")
    files.write(f"{reciever}")
    files.close()


def sendingEmail(config):

    api = "https://protected-shelf-73940.herokuapp.com/sendEmail"

    params = {"data": [config["email"], config["queueTime"]]}

    r = requests.post(url = api, data = params )

    result = r.text
    
    if(result != "Sent successfully!"):
        print("There was an error sending to your personal email")
    else:
        print(result)



