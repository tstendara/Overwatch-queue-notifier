import pyscreenshot as ImageGrab 
from PIL import Image
from sending import send
from helper import findFile
from conf import configuration
import smtplib, ssl
import time 


textingConfiguration = (configuration.TWILIO_SID != '' or configuration.TWILIO_TOKEN != '' or configuration.phoneNumber != '')
credentialFileExists = findFile()
credentials = {}
print(textingConfiguration)
# if both configs dont exist then dont let it go 
if(credentialFileExists == False and textingConfiguration == False):
    print("please run python setup.py first or setup messaging service in readMe")
    exit()
elif(credentialFileExists):
    fil = open("credentials.txt", "r")
    credentials["email"] = fil.readline()[:-2] # removing \n 
    credentials["password"] = fil.readline()
    print(credentials)
elif(textingConfiguration):
    print("gonna text")
    credentials["TWILIO_SID"] = configuration.TWILIO_SID
    credentials["TWILIO_TOKEN"] = configuration.TWILIO_TOKEN
    credentials["phoneNumber"] = configuration.phoneNumber
    
    
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

    fullTime = str(minutes) +':'+ str(sec)
    
    if(credentialFileExists):    
        send(fullTime, credentials) 
    else:
        send(fullTime, False)


    


    
