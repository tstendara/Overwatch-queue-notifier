def test():
    reading = open("credentials.txt", "r")
    email = reading.readline(1)
    passwd = reading.readline(2)

    print(email, passwd)