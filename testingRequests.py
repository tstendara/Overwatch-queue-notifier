import helper
import random 

def test():
    for x in range(100):
        queueTime = random.randint(0, 1000)
        helper.sendingEmail({"email":"test@email.com", "queueTime":""})

test()