from conf import configuration
from helper import findFile



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