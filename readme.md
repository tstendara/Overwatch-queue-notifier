# Configuration

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


# Email/Texting setup

1. Run this command:
```
python setup.py
```
Then enter your email/(Twilio SID, Twilio Token, Twilio number, and your personal number), and thats it for setup! Continue to [Start the Script](#Starting-the-Script)

-After running setup you'll be texted/emailed for a test.
<br />





# Starting the Script

1. Launch Overwatch and change it to bordless windowed so that you can start the script without closing the Overwatch window.

2. If you dont already have Powershell open, run: 
```
cd Downloads/Overwatch-queue-notifier-master/Overwatch-queue-notifier-master
```

3. Lastly run:
```
python watchingQueue.py
```

