from twilio.rest import Client
import smtplib, ssl
import helper

def send(data, email):
    if(email == False):
        client = Client(data["TWILIO_SID"], data["TWILIO_TOKEN"])
        message = client.messages \
            .create(
                body='       QUEUE TIME:  '+ data["queueTime"] + '     , Goodluck!',
                from_=data["TWILIO_NUMBER"],
                to=data["phoneNumber"]
            )
    else:
        # gonna send post requests here $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        # message = data["fulltime"]
        # reciever = data["email"]
        
        helper.sendingEmail(data)


        






        