import os 
from helper import findFile
import time

credentialFileExists = findFile()

if(credentialFileExists == True):
    os.system("del credentials.txt")    
    time.sleep(2)

os.system("echo test > credentials.txt")

files = open("credentials.txt", "w")
emailaddr = input("email adress: ")
password = input("password: ")

files.write(f"""{emailaddr} 
{password}""" )
# files.write(f"{password}")
files.close()

reading = open("credentials.txt", "r")
email = reading.readline()
passwd = reading.readline()

print(email, passwd)  


