import importlib
import userdata
import functions
import json
import os
import smtplib
import requests
import urllib
import time
import configs
from bs4 import BeautifulSoup
#from urllib import Request, urlopen
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date , timedelta , datetime

#TIME
start_time = time.time()
today=date.today()
present = today.strftime("%d-%m-20%y")
tomorrow = today + timedelta(1)
tomorrow = tomorrow.strftime("%d-%m-20%y")

if __name__ == '__main__':
    Center_set = set()
    count=0
    while True:
        #Clearing set of booked centres everyday at 00:00 - 00:01
        if(int(datetime.now().strftime("%H%M%S"))<100):
            print("\n \n Today's centers : ",Center_set)
            Center_set.clear()
            print("\n Set Cleared : ",Center_set)
            print("\n Current time : ",int(datetime.now().strftime("%H%M%S")))
        importlib.reload(userdata)
        importlib.reload(functions)
        userdata.CheckAvailability(count,Center_set)
        endtime=time.time()
        print("Runtime : ",endtime-start_time)
