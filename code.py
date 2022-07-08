from turtle import delay
import schedule 
import time 
import requests
from email.message import EmailMessage
import smtplib, ssl
from prettytable import PrettyTable



index = 0
while True:
    
    URL = "https://api.binance.com/api/v3/ticker/price"
  
    # location given here

    
    # defining a params dict for the parameters to be sent to the API
    
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL)

    data= r.json()
    
    
    ROC_List=[]
    from prettytable import PrettyTable
    A = PrettyTable()
    A.field_names= ["Symbol","ROC", "End Price", "Start Price"]
    if index != 0:
    
        for m,price in enumerate(last_price):
    
            previous= data[m]
            new= last_price[m]
        
            prev_price=( float(previous['price']))
            new_price= (float(new['price']))
            ROC= new_price - prev_price
            temp= {'symbol': previous['symbol'], 'ROC': ROC , "Start Price": prev_price, 'End Price': new_price}
            A.add_row([previous['symbol'], ROC, prev_price, new_price])
            
            ROC_List.append(temp)
        sorted_list=sorted(ROC_List, key=lambda x: x['ROC'], reverse=True)
        
        A = PrettyTable()
        A.field_names= ["*****Symbol*****","*****ROC*****", "****End Price****", "****Start Price****"]
        A.max_width['ROC'] = A.max_width['Symbol'] = 100
        A.max_table_width= 150
        for s in sorted_list:
            # strRW = '''<tr><td>"+s['symbol']+ "</td><td>"+str(s['ROC'])+"</td><td>"+str(s['Start Price'])+"</td><td>"+str(s['End Price'])+"</td></tr>'''
            # strTable = strTable+strRW
        

            A.add_row([s['symbol'],s['ROC'] , s['Start Price'], s['End Price']])
        content=(str(A))
        msg = EmailMessage()
        msg['Subject'] = 'Roc of all coins'
        msg['To'] = 'tjjaccrypto@gmail.com'
        msg.set_content(str(A))
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

    last_price= r.json()
    index +=1
    print (A)
    time.sleep(300)


