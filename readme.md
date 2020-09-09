# About
This app aides the problem with long queue times for dps on Overwatch. This software will notify the user upon finding a game with low latency giving the user the freedom to move freely from their pc, worry-free that they may get into a match unnoticed.  

- All user information is stored in plain .txt files on the users computer.

# Getting Started

1. [Install Python](https://www.python.org/downloads/) 

 - Open file and add to path

![GitHub Logo](/instructions/installpython.PNG)


2. From the root of `Overwatch-queue-notifier-master`, run 
```
python install -r requirements.txt
```


# Email/Text setup

Run the following command:
```
python setup.py
```

## Email 
```
[e] or [email]
```
You'll then be prompted to input your email, after entering your info. You wont need to run 
setup again unless you need to change the email or the way that you would like to be 
notified. 

## Text
```
[t] or [text]
```

In order to use the texting service, you must setup an account on https://www.twilio.com/. Then go to Dashboard -- there you'll find your Trial Number, Account SID and AUTH token which is all required for the text setup. You wont need to run setup again unless you need to change the personal or the way that you would like to be notified.

# Running the software

1. Change Overwatch display to windowed, or borderless
2. Navigate to Career profile
3. Open terminal(insure that the terminal window isn't on the top left of the screen) and run ```python watchingQueue.py``` 

Now go get something to eat, Jeff will let you know when you get into a game! 



