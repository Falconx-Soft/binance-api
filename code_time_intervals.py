from turtle import delay
import schedule 
import time 
import requests
from email.message import EmailMessage
import smtplib, ssl
from prettytable import PrettyTable
import random
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib,ssl

# ******** Australlian Dollar Rate According to US Dollar
aus_dollar= 1.48

URL_coins = "https://api.binance.com/api/v3/ticker/price"
r_coins = requests.get(url = URL_coins)
all_coins= r_coins.json()
print(all_coins)
list_of_coins=[]
for coin in all_coins:
    list_of_coins.append(coin['symbol'])

index = 0
while True:
    print('******************************* Start Loop *****************************')
    # *** Defining parameters

    chunks = [list_of_coins[x:x+100] for x in range(0, len(list_of_coins), 100)]

    #************************* Data For one Hour Time Interval
    print('**************************** 1h')
    data = []
    for index, chunk in enumerate(chunks):
        temp = '['
        count=1
        for c in chunk:
            # print('No.'+str(count), c)
            count+=1
            temp += '"'+str(c)+'"'
            temp += ','
        temp= temp.rstrip(',')
        temp += ']'
        
        # print(temp)
        # print(type(temp))
        return_data=requests.get(url = 'https://api.binance.com/api/v3/ticker?symbols='+temp+'&windowSize=1h')
        print(return_data.json())
        data+= return_data.json()
        if index == 10:
            time.sleep(60)
    # *************** End 1 Hour
    # *************** Data For 2 hour interval
    print('**************************** 2h')

    time.sleep(60)
    data_2h = []
    for index, chunk in enumerate(chunks):
        temp = '['
        count=1
        for c in chunk:
            # print('No.'+str(count), c)
            count+=1
            temp += '"'+str(c)+'"'
            temp += ','
        temp= temp.rstrip(',')
        temp += ']'
        
        # print(temp)
        # print(type(temp))
        return_data=requests.get(url = 'https://api.binance.com/api/v3/ticker?symbols='+temp+'&windowSize=2h')
        print(return_data.json())
        data_2h+= return_data.json()
        if index == 10:
            time.sleep(60)
    # *************** End 2 Hour
    # *************** Data For 4 hour interval
    print('**************************** 4h')

    time.sleep(60)
    data_4h = []
    for index, chunk in enumerate(chunks):
        temp = '['
        count=1
        for c in chunk:
            # print('No.'+str(count), c)
            count+=1
            temp += '"'+str(c)+'"'
            temp += ','
        temp= temp.rstrip(',')
        temp += ']'
        
        # print(temp)
        # print(type(temp))
        return_data=requests.get(url = 'https://api.binance.com/api/v3/ticker?symbols='+temp+'&windowSize=4h')
        print(return_data.json())
        data_4h+= return_data.json()
        if index == 10:
            time.sleep(60)
    # *************** End 4 Hour
    # *************** Data For 8 hour interval
    print('**************************** 8h')

    time.sleep(60)
    data_8h = []
    for index, chunk in enumerate(chunks):
        temp = '['
        count=1
        for c in chunk:
            # print('No.'+str(count), c)
            count+=1
            temp += '"'+str(c)+'"'
            temp += ','
        temp= temp.rstrip(',')
        temp += ']'
        
        # print(temp)
        # print(type(temp))
        return_data=requests.get(url = 'https://api.binance.com/api/v3/ticker?symbols='+temp+'&windowSize=4h')
        print(return_data.json())
        data_8h+= return_data.json()
        if index == 10:
            time.sleep(60)
    # *************** End 8 Hour
    
    #************************* Data For 24 Hour Time Interval
    print('**************************** 24h')
    time.sleep(60)
    data_24h = []
    for index, chunk in enumerate(chunks):
        temp = '['
        count=1
        for c in chunk:
            # print('No.'+str(count), c)
            count+=1
            temp += '"'+str(c)+'"'
            temp += ','
        temp= temp.rstrip(',')
        temp += ']'
        
        # print(temp)
        # print(type(temp))
        return_data=requests.get(url = 'https://api.binance.com/api/v3/ticker?symbols='+temp)
        print(return_data.json())
        data_24h+= return_data.json()
        if index == 10:
            time.sleep(60)
    # *************** End 24 Hour
    # *************** Data For 2 day interval
    print('**************************** 2d')
    time.sleep(60)
    data_2d = []
    for index, chunk in enumerate(chunks):
        temp = '['
        count=1
        for c in chunk:
            # print('No.'+str(count), c)
            count+=1
            temp += '"'+str(c)+'"'
            temp += ','
        temp= temp.rstrip(',')
        temp += ']'
        
        # print(temp)
        # print(type(temp))
        return_data=requests.get(url = 'https://api.binance.com/api/v3/ticker?symbols='+temp+'&windowSize=2d')
        print(return_data.json())
        data_2d+= return_data.json()
        if index == 10:
            time.sleep(60)
    # *************** End 2 day
    # *************** Data For 3 day interval
    print('**************************** 3d')
    time.sleep(60)
    data_3d = []
    for index, chunk in enumerate(chunks):
        temp = '['
        count=1
        for c in chunk:
            # print('No.'+str(count), c)
            count+=1
            temp += '"'+str(c)+'"'
            temp += ','
        temp= temp.rstrip(',')
        temp += ']'
        
        # print(temp)
        # print(type(temp))
        return_data=requests.get(url = 'https://api.binance.com/api/v3/ticker?symbols='+temp+'&windowSize=3d')
        print(return_data.json())
        data_3d+= return_data.json()
        if index == 10:
            time.sleep(60)
    # *************** End 3 day
    # *************** Data For 5 day interval
    print('**************************** 5d')
    time.sleep(60)
    data_5d = []
    for index, chunk in enumerate(chunks):
        temp = '['
        count=1
        for c in chunk:
            # print('No.'+str(count), c)
            count+=1
            temp += '"'+str(c)+'"'
            temp += ','
        temp= temp.rstrip(',')
        temp += ']'
        
        # print(temp)
        # print(type(temp))
        return_data=requests.get(url = 'https://api.binance.com/api/v3/ticker?symbols='+temp+'&windowSize=5d')
        print(return_data.json())
        data_5d+= return_data.json()
        if index == 10:
            time.sleep(60)
    # *************** End 5 day
    
    
    print('***********************************************************')
    # print(data)
    # print(type(data))
    # *************** Sorted List For 1 Hour
    sorted_list=sorted(data, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # *************** Sorted List For 2 Hour
    sorted_list_2h=sorted(data_2h, key=lambda x: abs(float(x['priceChange'])), reverse=True)
    
     # *************** Sorted List For 4 Hour
    sorted_list_4h=sorted(data_4h, key=lambda x: abs(float(x['priceChange'])), reverse=True)

    # *************** Sorted List For 8 Hour
    sorted_list_8h=sorted(data_8h, key=lambda x: abs(float(x['priceChange'])), reverse=True)

    # *************** Sorted List For 24 Hour
    sorted_list_24h=sorted(data_24h, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # *************** Sorted List For 2 day
    sorted_list_2d=sorted(data_2d, key=lambda x: abs(float(x['priceChange'])), reverse=True)
    
     # *************** Sorted List For 3 day
    sorted_list_3d=sorted(data_3d, key=lambda x: abs(float(x['priceChange'])), reverse=True)

    # *************** Sorted List For 5 day
    sorted_list_5d=sorted(data_5d, key=lambda x: abs(float(x['priceChange'])), reverse=True)



    # ****************************** Creating CSVs*******************************************
    
    
    n = random.randint(0,100000)
    fields = ['symbol', 'priceChange', 'priceChangePercent', 'openPrice', 'lastPrice']
    
    # One Hour Change
    name_of_csv_1h= 'Data Of 1 Hour Change_'+ str(n)+'.csv'
    with open(str(name_of_csv_1h), 'w', newline='',errors="ignore") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames= fields, extrasaction='ignore')
            dict_writer.writeheader()
            dict_writer.writerows(sorted_list)
    # 2 Hour Change
    name_of_csv_2h= 'Data Of 2 Hour Change_'+ str(n)+'.csv'
    with open(str(name_of_csv_2h), 'w', newline='',errors="ignore") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames= fields, extrasaction='ignore')
            dict_writer.writeheader()
            dict_writer.writerows(sorted_list_2h)
    # 4 Hour Change
    name_of_csv_4h= 'Data Of 4 Hour Change_'+ str(n)+'.csv'
    with open(str(name_of_csv_4h), 'w', newline='',errors="ignore") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames= fields, extrasaction='ignore')
            dict_writer.writeheader()
            dict_writer.writerows(sorted_list_4h)
    # 8 Hour Change
    name_of_csv_8h= 'Data Of 8 Hour Change_'+ str(n)+'.csv'
    with open(str(name_of_csv_8h), 'w', newline='',errors="ignore") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames= fields, extrasaction='ignore')
            dict_writer.writeheader()
            dict_writer.writerows(sorted_list_8h)
    # 24 Hour Change
    name_of_csv_24h= 'Data Of 24 Hour Change_'+ str(n)+'.csv'
    with open(str(name_of_csv_24h), 'w', newline='',errors="ignore") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames= fields, extrasaction='ignore')
            dict_writer.writeheader()
            dict_writer.writerows(sorted_list_24h)
    # 2 Days Change
    name_of_csv_2d= 'Data Of 2 Days Change_'+ str(n)+'.csv'
    with open(str(name_of_csv_2d), 'w', newline='',errors="ignore") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames= fields, extrasaction='ignore')
            dict_writer.writeheader()
            dict_writer.writerows(sorted_list_2d)
    # 3 Days Change
    name_of_csv_3d= 'Data Of 3 Days Change_'+ str(n)+'.csv'
    with open(str(name_of_csv_3d), 'w', newline='',errors="ignore") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames= fields, extrasaction='ignore')
            dict_writer.writeheader()
            dict_writer.writerows(sorted_list_3d)
    # 5 Days Change
    name_of_csv_5d= 'Data Of 5 Days Change_'+ str(n)+'.csv'
    with open(str(name_of_csv_5d), 'w', newline='',errors="ignore") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames= fields, extrasaction='ignore')
            dict_writer.writeheader()
            dict_writer.writerows(sorted_list_5d)
    
    # ************************** Sending Emails ******************************

    # ************ Email For 1 Hour
    msg = MIMEMultipart()
    body_part = MIMEText('plain')
    msg['Subject'] = '1 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(str(name_of_csv_1h),'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=str(name_of_csv_1h)))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kabocha608@gmail.com"
    password = 'oatomvjfzesuawvu'
    context = ssl.create_default_context()
    try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.send_message(msg)
            

    except Exception as e:
            # Print any error messages to stdout
            print('************')
            print('Exception',e)
    finally:
            server.quit()

    # ************ Email For 2 Hour
    msg = MIMEMultipart()
    body_part = MIMEText('plain')
    msg['Subject'] = '2 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(str(name_of_csv_2h),'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=str(name_of_csv_2h)))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kabocha608@gmail.com"
    password = 'oatomvjfzesuawvu'
    context = ssl.create_default_context()
    try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.send_message(msg)
            

    except Exception as e:
            # Print any error messages to stdout
            print('************')
            print('Exception',e)
    finally:
            server.quit()
    

    # ************ Email For 4 Hour
    msg = MIMEMultipart()
    body_part = MIMEText('plain')
    msg['Subject'] = '4 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(str(name_of_csv_4h),'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=str(name_of_csv_4h)))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kabocha608@gmail.com"
    password = 'oatomvjfzesuawvu'
    context = ssl.create_default_context()
    try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.send_message(msg)
            

    except Exception as e:
            # Print any error messages to stdout
            print('************')
            print('Exception',e)
    finally:
            server.quit()
    
    # ************ Email For 8 Hour
    msg = MIMEMultipart()
    body_part = MIMEText('plain')
    msg['Subject'] = '8 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(str(name_of_csv_8h),'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=str(name_of_csv_8h)))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kabocha608@gmail.com"
    password = 'oatomvjfzesuawvu'
    context = ssl.create_default_context()
    try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.send_message(msg)
            

    except Exception as e:
            # Print any error messages to stdout
            print('************')
            print('Exception',e)
    finally:
            server.quit()

    # ************ Email For 24 Hour
    msg = MIMEMultipart()
    body_part = MIMEText('plain')
    msg['Subject'] = '1 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(str(name_of_csv_24h),'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=str(name_of_csv_24h)))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kabocha608@gmail.com"
    password = 'oatomvjfzesuawvu'
    context = ssl.create_default_context()
    try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.send_message(msg)
            

    except Exception as e:
            # Print any error messages to stdout
            print('************')
            print('Exception',e)
    finally:
            server.quit()
    

    # ************ Email For 2 Days
    msg = MIMEMultipart()
    body_part = MIMEText('plain')
    msg['Subject'] = '2 Days Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(str(name_of_csv_2d),'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=str(name_of_csv_2d)))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kabocha608@gmail.com"
    password = 'oatomvjfzesuawvu'
    context = ssl.create_default_context()
    try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.send_message(msg)
            

    except Exception as e:
            # Print any error messages to stdout
            print('************')
            print('Exception',e)
    finally:
            server.quit()
    

    # ************ Email For 3 Days
    msg = MIMEMultipart()
    body_part = MIMEText('plain')
    msg['Subject'] = '3 Days Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(str(name_of_csv_3d),'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=str(name_of_csv_3d)))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kabocha608@gmail.com"
    password = 'oatomvjfzesuawvu'
    context = ssl.create_default_context()
    try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.send_message(msg)
            

    except Exception as e:
            # Print any error messages to stdout
            print('************')
            print('Exception',e)
    finally:
            server.quit()

    # ************ Email For 5 Days
    msg = MIMEMultipart()
    body_part = MIMEText('plain')
    msg['Subject'] = '5 Days Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(str(name_of_csv_5d),'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=str(name_of_csv_5d)))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "kabocha608@gmail.com"
    password = 'oatomvjfzesuawvu'
    context = ssl.create_default_context()
    try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.send_message(msg)
            

    except Exception as e:
            # Print any error messages to stdout
            print('************')
            print('Exception',e)
    finally:
            server.quit()
    print('******************************* End Loop *****************************')

    
