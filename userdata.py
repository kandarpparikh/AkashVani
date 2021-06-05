import importlib
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

#PINCODES
pin_array_john=[400067,400064]
pin_array_doe=[380015,380052]

#EMAILS
email_john="kirandhamal@gmail.com"
email_doe="dpdhruvprajapati@gmail.com"

#TIME
start_time = time.time()
today=date.today()
present = today.strftime("%d-%m-20%y")
tomorrow = today + timedelta(1)
tomorrow = tomorrow.strftime("%d-%m-20%y")

#HEADERS
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)    Chrome/41.0.2228.0 Safari/537.36'}

#Function call
def CheckAvailability(count,Center_set):
    importlib.reload(functions)
    functions.CallApi(headers,pin_array_john,tomorrow,count,email_john,Center_set)
    functions.stats(Center_set)
    functions.CallApi(headers,pin_array_doe,tomorrow,count,email_doe,Center_set)
    functions.stats(Center_set)
