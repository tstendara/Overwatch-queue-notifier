import os 

os.system("echo test > credentials.txt")

file = open("credentials.txt", "w")
emailaddr = input("email adress: ")
password = input("password: ")

file.write(f"{emailaddr}")
file.write("\n" + f"{password}")
file.close()

reading = open("credentials.txt", "r")
email = reading.readline(1)
passwd = reading.readline(2)

