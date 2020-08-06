# About
This app solves the problem with long queue times for dps on Overwatch utilizing this notification system which will notify the user upon finding a game with low latency. 

* All user information is stored in plain .txt files on the users computer.

# Getting Started

1. [Install Python](https://www.python.org/downloads/) 

 - Open file and add to path

![GitHub Logo](/instructions/installpython.PNG)

2. download file as zip and save file

![GitHub Logo](/instructions/download.PNG)

3. Open your Downloads folder, right click ```Overwatch-queue-notifier.zip ``` and click extract all. This will extract everything to the Downloads folder by default.

4. Then open powershell by going to the search bar at the bottom left of your screen. Windows PowerShell and open it. Then run these commands: 
```
cd Downloads/Overwatch-queue-notifier-master/Overwatch-queue-notifier-master

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



