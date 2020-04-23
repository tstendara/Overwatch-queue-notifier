import pyscreenshot as ImageGrab 
from PIL import Image
from sending import send
from helper import findFile
import smtplib, ssl
import time 

credentialFileExists = findFile()
credentials = {}

if(credentialFileExists == False):
    print("please run python setup.py first")
    exit()
else:
    fil = open("credentials.txt", "r")
    credentials["email"] = fil.readline()[:-2] # removing \n 
    credentials["password"] = fil.readline()
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

    fullTime = str(minutes) +':'+ str(sec)
    
    send(fullTime) 



    


    
