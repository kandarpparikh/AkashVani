# AkashVani
is a word of Sanskrit origin meaning "celestial announcement", or "voice from the sky/heaven" .  As there is low supply and high demand for vaccines , it is difficult to book slots for vaccination on cowin website. This project would notify the user via mail as soon as the vaccine slot is available in the nearby areas which are defined by pincodes. It notifies the user via mail about the vaccines which can save lives , thus the project name is AkashVani , considering the vaccine notification as a notification from heaven.

# How To Use

## Install all the dependencies (use cmd in windows)
```
pip3 install -r requirements.txt
```
## Configurations (FILE : configs.py)
- Open configs.py and Set your Gmail and password between the "" (Quotes) . This will be the Mail-Id from where the Vaccine Availability Notifications will be originating. You can also configure your secondary email as test email . Whenever a Vaccine Availabilty Notification is sent , your test mail will also receive it as it will be in CC .
```
#Set password of origin email
password="My-Password"

#Set origin emailId
username="My-Gmail-ID"

#testinng mail ID
testmail="OPTIONAL-MAIL-ID"
```

## Change Google security settings of Originating Email-ID that you just set in configs.py
- This is to allow the script to send the mails 
- Visit the below link and Turn OFF "2-Step verification" if already set and Turn ON "Less secure app access"
 https://myaccount.google.com/security?pli=1
 
## Configure receipent's Mail-IDs and Pincodes (File: userdata.py)
- Open userdata.py and set receipents mail id and Pincodes by creating their array. You can add multiple arrays and multiple pincodes
```
#PINCODES
pin_array_john=[400067,400064]
pin_array_doe=[380015,380052]

#EMAILS
email_john="kirandhamal@gmail.com"
email_doe="dpdhruvprajapati@gmail.com"
```
- In userdata.py under function CheckAvailability() , Add function call in the below mentioned way
```
    functions.CallApi(headers,pin_array_john,tomorrow,count,email_john,Center_set)
    functions.stats(Center_set)
    functions.CallApi(headers,pin_array_doe,tomorrow,count,email_doe,Center_set)
    functions.stats(Center_set)
```
- Here "tomorrow" denotes that the script will check slot availabilty for tomorrow . you can also replace it with "present" to make it check for today.

# Run the Python file (FINAL STEP , After this sit back and relax)
- This will ensure that the python file keeps on running even if ssh session ends or you quit the server. 
- If you are running the script on windows (Personal Computer) , you will have to keep the Laptop ON.
```
nohup python3 -u main.py > output.log &
```

# Log file
- Logs are logged in output.log file
- To have a quick view of logs , you can execute the below command
```
tail -f output.log
```

- It should look like the below output:
```
-----------------------------------------------------------
{518242, 518243, 711402, 711387, 711405, 670870, 518234, 518235, 700926}
400067
200
word length 0
Pause & avoid [403] , 3 secs
-----------------------------------------------------------
400064
200
word length 0
Pause & avoid [403] , 3 secs
-----------------------------------------------------------
{518242, 518243, 711402, 711387, 711405, 670870, 518234, 518235, 700926}
400067
200
word length 0
Pause & avoid [403] , 3 secs
-----------------------------------------------------------
400064
200
word length 0
Pause & avoid [403] , 3 secs
-----------------------------------------------------------
{518242, 518243, 711402, 711387, 711405, 670870, 518234, 518235, 700926}
Runtime :  230308.29872441292
380008
200
word length 0
Pause & avoid [403] , 3 secs
```

# Add or remove EmailId or Pincodes
- You can add or remove Email-IDs or/and Pincodes from userdata.py while the script is running . No need to stop the script for this.

# Kill the Process
- If you decide to stop the script use the below process.
- To stop the script on server 
```
pkill -f main.py
```
- Remove the log file
```
rm -rf output.log 
```

