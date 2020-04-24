import os 
import helper
import time

credentialFileExists = helper.findFile()

if(credentialFileExists == True):
    os.system("del credentials.txt")    
    time.sleep(2)

os.system("echo test > credentials.txt")
emailormessage = input("would you like to be notified via text or email? (Enter e or email for email and t or text for text):  ")

if (emailormessage == "email"):
    emailormessage = 'e'
elif(emailormessage == 'text'):
    emailormessage = 't'

if (emailormessage == 'e'):
    sender_email = input("senders email adress: ")
    sender_password = input("senders password: ")
    reciever_email = input("recievers email: ")
    helper.email(emailormessage, sender_email, sender_password, reciever_email)
elif(emailormessage == 't'):
    Twilio_number = input("Twilio Number: ")
    Twilio_sid = input("Twilio SID: ") 
    Twilio_token = input("Twilio Token: ")
    personalNumber = input("Personal Number: ")
    helper.text(emailormessage, Twilio_number, Twilio_sid, Twilio_token, personalNumber)
else:
    print("please enter e/email for email or t/text for text")

