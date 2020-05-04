import pyscreenshot as ImageGrab 
from PIL import Image
import helper 
import smtplib, ssl
import time 

start = time.time() #queue time

config_does_exist = helper.findFile()
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
    print("Will notify via", x.readline().strip() + "mail")
    credentials["email"] = x.readline().strip()  
elif(emailortext == 't'):
    print("Will notify via", x.readline().strip() + "ext" )
    credentials["TWILIO_NUMBER"] = x.readline().strip()
    credentials["TWILIO_SID"] = x.readline().strip()
    credentials["TWILIO_TOKEN"] = x.readline().strip()
    credentials["phoneNumber"] = x.readline().strip()


print("Jeff will let you know when you're in a game!")

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

    credentials["queueTime"] = 'QUEUE TIME: '+ str(minutes) +':'+ str(sec) + ', Goodluck!'
    
    if(emailortext == 'e'):    
        helper.sendingEmail(credentials) 
    else:
        helper.sendingText(credentials)


    


    
