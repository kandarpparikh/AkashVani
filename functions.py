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


def CallApi(headers,pincodes,tomorrow,mycount,thismail,Center_set):

    #Check by hitting api for each pincode if session is availablee or not
    for mypincode in pincodes:
        print(mypincode)
        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={0}&date={1}'.format(str(mypincode), tomorrow)
        response = requests.get(url ,headers = headers)
        print(response.status_code)
        if(response.status_code==200):
            data = response.json()
            getData(data,thismail,Center_set)
        else:
            print("API call not successfull")
        print("Pause & avoid [403] , 3 secs")
        print("-----------------------------------------------------------")
        time.sleep(3)


def getData(api_data,thismail,Center_set):
    for i in api_data['sessions']:
        #Check if Age limit is 18 , Center has not beeen opened for booking already and available vaccine count is > 5
        if (i['min_age_limit'] == 18) and (i['center_id'] not in Center_set) and (i["available_capacity"] > 5):
            now=time.localtime()
            current_time = time.strftime("%H:%M:%S",now)
            #Add centerId in set which states that the center has been already opened for booking
            Center_set.add(i['center_id'])
            #Open Text file to write the data extracted from API
            text_file = open("sessions.json", "a")
            text_file.write("Slot opened at : "+current_time+"\n")
            text_file.write("Center Name :" +str(i['name'])+"\n")
            text_file.write("Pincode :" +str(i['pincode'])+"\n")
            text_file.write("Name of Vaccine : "+str(i['vaccine']) +"\n")
            text_file.write("Vaccines Available for DOSE 1: " +str(i['available_capacity_dose1'])+"\n")
            text_file.write("Vaccines Available for DOSE 2: " +str(i['available_capacity_dose2'])+"\n")
            text_file.write("Book your slot at https://selfregistration.cowin.gov.in/"+"\n")
            text_file.write("Call/Msg OR Whatsapp on 9712586540 to stop the Email notifications , Please also mention your MailId"+"\n")
            text_file.close()
            print("\n Pincode : ",i['pincode'])
            print(" Name : ",i['name'])
            print("\n Vaccines available : ",i['available_capacity'])
    #Send mail for thee pincode where vaccine is available
    sendmail(thismail)

def sendmail(recievermail):
    #Open textfile and check if data is present 
    text_file = open("sessions.json", "rt")
    data = text_file.read()
    words = data.split()
    print("word length",len(words))
    #If data is present then initiate Mail and send mail to the receiver with smtp protocols
    if(len(words)>0):
        print("--Initiate Email Session--")

        sender_email = configs.username
        receiver_email=[]
        receiver_email.append(str(recievermail))
        receiver_email.append(configs.testmail)
        print("Reciever mail : ",receiver_email[0])
        print("Reciever mail : ",receiver_email[1])
        password = configs.password

        message = MIMEMultipart("alternative")
        message["Subject"] = "Vaccine Availability Notification"
        message["From"] = sender_email
        message["To"] = ", ".join(receiver_email)

        part1 = MIMEText(data, "plain")
        message.attach(part1)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        receiver_email.clear()
    #Clear contents from the file after the mail has been sent
    f = open('sessions.json', 'r+')
    f.truncate(0)
    f.close()


def stats(Center_set):
    print(Center_set)

