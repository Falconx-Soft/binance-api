from turtle import delay
import schedule 
import time 
import requests
from email.message import EmailMessage
import smtplib, ssl
from prettytable import PrettyTable




index = 0
while True:
    print('******************************* Start Loop *****************************')
    
    URL = "https://api.binance.com/api/v3/ticker/price"
  
    # location given here

    
    # defining a params dict for the parameters to be sent to the API
    
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)

    data= r.json()
    
    
    ROC_List=[]
    Aust_roc_list= []
    
 
   
    if index != 0:
    
        for m,price in enumerate(last_price):
    
            previous= data[m]
            new= last_price[m]
        
            prev_price=( float(previous['price']))
            aust_prev_price= ( float(previous['price']))*(1.46)

            new_price= (float(new['price']))
            aust_new_price= (float(new['price']))*(1.46)
            
            ROC= new_price - prev_price
            Aust_Roc= aust_new_price- aust_prev_price
            
            Roc_percent= ((new_price - prev_price)/prev_price)*100
            aust_Roc_percent= ((aust_new_price - aust_prev_price)/aust_prev_price)*100
            
            temp= {'symbol': previous['symbol'], 'ROC': ROC , "Start Price": prev_price, 'End Price': new_price, 'Percentage Change': str(Roc_percent) + '%'}
            aust_temp= {'symbol': previous['symbol'], 'ROC': Aust_Roc , "Start Price": aust_prev_price, 'End Price': aust_new_price, 'Percentage Change': str(aust_Roc_percent)+'%'}

            
            
            ROC_List.append(temp)
            Aust_roc_list.append(aust_temp)
        
        aust_sorted_list=sorted(Aust_roc_list, key=lambda x: x['ROC'], reverse=True)
        sorted_list=sorted(ROC_List, key=lambda x: x['ROC'], reverse=True)
        
        A = PrettyTable()
        Aust_table = PrettyTable()
        
        A.title = ' US Dollar Rate'
        Aust_table.title= "Australian Dollar Rate"
        
        A.field_names= ["*****Symbol*****","*****ROC*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
        Aust_table.field_names= ["*****Symbol*****","*****ROC*****", "****Start Price****", "****End Price****", "*****Percentage Change*****"]
        
        
        A.max_width['ROC'] = A.max_width['Symbol'] = 100
        A.max_table_width= 150
        Aust_table.max_width['ROC'] = A.max_width['Symbol'] = 100
        Aust_table.max_table_width= 150
        
        for s in sorted_list[:5]:
            A.add_row([s['symbol'],s['ROC'] , s['Start Price'], s['End Price'], s['Percentage Change']])
        for aust_s in aust_sorted_list[:5]:
            Aust_table.add_row([aust_s['symbol'],aust_s['ROC'] ,aust_s['Start Price'], aust_s['End Price'], aust_s['Percentage Change']])

        content=(str(A)+ str(Aust_table))
        msg = EmailMessage()
        msg['Subject'] = 'Roc of all coins'
        msg['To'] = 'mehrankhan6799@gmail.com'
        msg.set_content(str(A)+ str(Aust_table))
        print('msg',msg)
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
                print('Exception',e)
        finally:
                server.quit()
        print(A)
        print(Aust_table)
    last_price= r.json()
    index +=1
    print('******************************* End Loop *****************************')
    time.sleep(20)


