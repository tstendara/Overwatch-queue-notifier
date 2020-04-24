import pyscreenshot as ImageGrab 
from PIL import Image
from sending import send
from helper import findFile
import smtplib, ssl
import time 

config_does_exist = findFile()
credentials = {}
if(config_does_exist):
    opening = open("credentials.txt", "r")
    emailortext = opening.readline().strip()
else:
    print("please run python setup.py first or setup messaging service in readMe")
    exit()

# if both configs dont exist then dont let it go 
x = open("credentials.txt", "r")

if(emailortext == 'e'):
    credentials["email"] = x.readline().strip()  
    credentials["password"] = x.readline().strip()
    print(credentials)
elif(emailortext == 't'):
    
    print(x.readline())
    credentials["TWILIO_NUMBER"] = x.readline().strip()
    credentials["TWILIO_SID"] = x.readline().strip()
    credentials["TWILIO_TOKEN"] = x.readline().strip()
    credentials["phoneNumber"] = x.readline().strip()
    print(credentials)

    
start = time.time() #queue time
print("I'll let you know when you're in a game!")

if __name__ == '__main__':
    keepRunning = True
    im = ImageGrab.grab()
    pix_val = list(im.getdata())
    pix_val_flat = [x for sets in pix_val for x in sets]
    last = pix_val_flat[500] #find better way to get top right pixel for different resolutions and aspect ratios
    
    while keepRunning:
        im = ImageGrab.grab()
        pix_val = list(im.getdata())
        pix_val_flat = [x for sets in pix_val for x in sets]
        cur = pix_val_flat[500]
        
        if last != cur:
            keepRunning = False

    end = time.time()
    queueTime = (round(end - start))
    remainder = queueTime%60

    if queueTime == remainder:
        minutes = 0
        sec = queueTime
    else:
        minutes = round(abs(remainder - queueTime))/60
        queueTime -= minutes*60
        sec = remainder

    credentials["fulltime"] = str(minutes) +':'+ str(sec)
    
    if(emailortext == 'e'):    
        send(credentials, True) 
    else:
        send(credentials, False)


    


    
