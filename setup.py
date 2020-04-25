import os 
import helper
import time

credentialFileExists = helper.findFile()

emailormessage = input("would you like to be notified via text or email? (Enter e or email for email and t or text for text):  ")

if (emailormessage == "email"):
    emailormessage = 'e'
elif(emailormessage == 'text'):
    emailormessage = 't'
elif(emailormessage != 'e' and emailormessage != 't'):
    print("please enter e/email for email or t/text for text")
    exit()

if(credentialFileExists == True):
    os.system("del credentials.txt")    

if (emailormessage == 'e'):
    reciever_email = input("peronal email: ")
    helper.email(emailormessage, reciever_email)
elif(emailormessage == 't'):
    Twilio_number = input("Twilio Number: ")
    Twilio_sid = input("Twilio SID: ") 
    Twilio_token = input("Twilio Token: ")
    personalNumber = input("Personal Number: ")
    helper.text(emailormessage, Twilio_number, Twilio_sid, Twilio_token, personalNumber)

    

