from conf import configuration
from twilio.rest import Client
import smtplib, ssl


def send(data, email):
    if(email == False):
        client = Client(data["TWILIO_SID"], data["TWILIO_TOKEN"])
        message = client.messages \
            .create(
                body='       QUEUE TIME:  '+ data["fulltime"] + '     , Goodluck!',
                from_=data["TWILIO_NUMBER"],
                to=data["phoneNumber"]
            )
    else:
        username = configuration.senderEmail
        password = configuration.senderPass
        message = configuration.message

        reciever = configuration.receiverEmail

        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email = username
        password = password

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            # TODO: Send email here
            server.sendmail(sender_email, reciever, message)
        except Exception as e:

            # Print any error messages to stdout
            print(e)
        finally:
            server.quit() 