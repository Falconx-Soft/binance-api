from turtle import delay
import schedule 
import time 
import requests
from email.message import EmailMessage
import smtplib, ssl
from prettytable import PrettyTable

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
    
    # **************** Table For 1 Hour
    A = PrettyTable()
    A.title = ' One Hour Change in Prices'

    A.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    A.max_table_width= 150

    Aust = PrettyTable()
    Aust.title = ' One Hour Change in Prices ( Australian Dollar)'

    Aust.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust.max_table_width= 150

    for s in sorted_list[:5]:
        A.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    #  **************** End Table 1 hour
    # ***************** Table For 2 Hour
    
    A_2h = PrettyTable()
    A_2h.title = ' Two Hour Change in Prices'

    A_2h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    A_2h.max_table_width= 150

    Aust_2h = PrettyTable()
    Aust_2h.title = ' Two Hour Change in Prices ( Australian Dollar)'

    Aust_2h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_2h.max_table_width= 150

    for s in sorted_list_2h[:5]:
        A_2h.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_2h.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ***************** End Table 2 Hour 
        # ***************** Table For 4 Hour
    
    A_4h = PrettyTable()
    A_4h.title = ' Four Hour Change in Prices'

    A_4h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    A_4h.max_table_width= 150

    Aust_4h = PrettyTable()
    Aust_4h.title = ' Four Hour Change in Prices ( Australian Dollar)'

    Aust_4h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_4h.max_table_width= 150

    for s in sorted_list_4h[:5]:
        A_4h.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_4h.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ***************** End Table 4 Hour 
        # ***************** Table For 8 Hour
    
    A_8h = PrettyTable()
    A_8h.title = ' Eight Hour Change in Prices'

    A_8h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    A_8h.max_table_width= 150

    Aust_8h = PrettyTable()
    Aust_8h.title = ' Eight Hour Change in Prices ( Australian Dollar)'

    Aust_8h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_8h.max_table_width= 150

    for s in sorted_list_8h[:5]:
        A_8h.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_8h.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ***************** End Table 8 Hour 
    

    # **************** Table For 24 Hour
    A_24h = PrettyTable()
    A_24h.title = ' 24 Hour Change in Prices'

    A_24h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    A_24h.max_table_width= 150

    Aust_24h = PrettyTable()
    Aust_24h.title = ' 24 Hour Change in Prices ( Australian Dollar)'

    Aust_24h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_24h.max_table_width= 150

    for s in sorted_list_24h[:5]:
        A_24h.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_24h.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    #  **************** End Table 24 hour
    # ***************** Table For 2 day
    
    A_2d = PrettyTable()
    A_2d.title = ' Two day Change in Prices'

    A_2d.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    A_2d.max_table_width= 150

    Aust_2d = PrettyTable()
    Aust_2d.title = ' Two day Change in Prices ( Australian Dollar)'

    Aust_2d.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_2d.max_table_width= 150

    for s in sorted_list_2d[:5]:
        A_2d.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_2d.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ***************** End Table 2 day 
        # ***************** Table For 3 day
    
    A_3d = PrettyTable()
    A_3d.title = ' Three Day Change in Prices'

    A_3d.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    A_3d.max_table_width= 150

    Aust_3d = PrettyTable()
    Aust_3d.title = ' Three day Change in Prices ( Australian Dollar)'

    Aust_3d.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_3d.max_table_width= 150

    for s in sorted_list_3d[:5]:
        A_3d.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_3d.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ***************** End Table 3 days 
        # ***************** Table For 5 days
    
    A_5d = PrettyTable()
    A_5d.title = ' Five day Change in Prices'

    A_5d.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    A_5d.max_table_width= 150

    Aust_5d = PrettyTable()
    Aust_5d.title = ' Five Day Change in Prices ( Australian Dollar)'

    Aust_5d.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_5d.max_table_width= 150

    for s in sorted_list_5d[:5]:
        A_5d.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_5d.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ***************** End Table 5 day 
    
    # print(A)
    # print(Aust)

    # ***************** For USDT as Base Coin (For 1 Hour)
    base_list= []
    for base_index,  base_coin in enumerate(sorted_list):
        if ( base_coin['symbol'].endswith('USDT')):
            temp_1= sorted_list[base_index]
            base_list.append(temp_1)
    sorted_list_base=sorted(base_list, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # For USDT as Base Coin ******* Table
    A_base = PrettyTable()
    Aust_base = PrettyTable()
    A_base.title = ' One Hour Change in Prices (USDT)'
    Aust_base.title = ' One Hour Change in Prices Australian Dollar  (USDT)'
    A_base.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_base.field_names= ["*****Symbol*****","*****priceChange*****", "****Start Price****", "****End Price****", "*****Percentage Change*****"]
        
    for s in sorted_list_base[:5]:
        A_base.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_base.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ************** End USTD Table 1 hour
    # ***************** For USDT as Base Coin (For 2 Hour)
    base_list= []
    for base_index,  base_coin in enumerate(sorted_list_2h):
        if ( base_coin['symbol'].endswith('USDT')):
            temp_1= sorted_list_2h[base_index]
            base_list.append(temp_1)
    sorted_list_base=sorted(base_list, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # For USDT as Base Coin ******* Table
    A_base_2h = PrettyTable()
    Aust_base_2h = PrettyTable()
    A_base_2h.title = ' Two Hour Change in Prices (USDT)'
    Aust_base_2h.title = ' Two Hour Change in Prices Australian Dollar  (USDT)'
    A_base_2h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_base_2h.field_names= ["*****Symbol*****","*****priceChange*****", "****Start Price****", "****End Price****", "*****Percentage Change*****"]
        
    for s in sorted_list_base[:5]:
        A_base_2h.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_base_2h.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ************** End USTD Table 2 hour
    # ***************** For USDT as Base Coin (For 4 Hour)
    base_list= []
    for base_index,  base_coin in enumerate(sorted_list_4h):
        if ( base_coin['symbol'].endswith('USDT')):
            temp_1= sorted_list_4h[base_index]
            base_list.append(temp_1)
    sorted_list_base=sorted(base_list, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # For USDT as Base Coin ******* Table
    A_base_4h = PrettyTable()
    Aust_base_4h = PrettyTable()
    A_base_4h.title = ' Four Hour Change in Prices (USDT)'
    Aust_base_4h.title = ' Four Hour Change in Prices Australian Dollar  (USDT)'
    A_base_4h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_base_4h.field_names= ["*****Symbol*****","*****priceChange*****", "****Start Price****", "****End Price****", "*****Percentage Change*****"]
        
    for s in sorted_list_base[:5]:
        A_base_4h.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_base_4h.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ************** End USTD Table 4 hour
    # ***************** For USDT as Base Coin (For 8 Hour)
    base_list= []
    for base_index,  base_coin in enumerate(sorted_list_8h):
        if ( base_coin['symbol'].endswith('USDT')):
            temp_1= sorted_list_8h[base_index]
            base_list.append(temp_1)
    sorted_list_base=sorted(base_list, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # For USDT as Base Coin ******* Table
    A_base_8h = PrettyTable()
    Aust_base_8h = PrettyTable()
    A_base_8h.title = ' Eight Hour Change in Prices (USDT)'
    Aust_base_8h.title = ' Eight Hour Change in Prices Australian Dollar  (USDT)'
    A_base_8h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_base_8h.field_names= ["*****Symbol*****","*****priceChange*****", "****Start Price****", "****End Price****", "*****Percentage Change*****"]
        
    for s in sorted_list_base[:5]:
        A_base_8h.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_base_8h.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ************** End USTD Table 8 hour
# ***************** For USDT as Base Coin (For 24 Hour)
    base_list= []
    for base_index,  base_coin in enumerate(sorted_list_24h):
        if ( base_coin['symbol'].endswith('USDT')):
            temp_1= sorted_list_24h[base_index]
            base_list.append(temp_1)
    sorted_list_base=sorted(base_list, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # For USDT as Base Coin ******* Table
    A_base_24h = PrettyTable()
    Aust_base_24h = PrettyTable()
    A_base_24h.title = ' 24 Hour Change in Prices (USDT)'
    Aust_base_24h.title = ' 24 Hour Change in Prices Australian Dollar  (USDT)'
    A_base_24h.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_base_24h.field_names= ["*****Symbol*****","*****priceChange*****", "****Start Price****", "****End Price****", "*****Percentage Change*****"]
        
    for s in sorted_list_base[:5]:
        A_base_24h.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_base_24h.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ************** End USTD Table 24 hour
    # ***************** For USDT as Base Coin (For 2 day)
    base_list= []
    for base_index,  base_coin in enumerate(sorted_list_2d):
        if ( base_coin['symbol'].endswith('USDT')):
            temp_1= sorted_list_2d[base_index]
            base_list.append(temp_1)
    sorted_list_base=sorted(base_list, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # For USDT as Base Coin ******* Table
    A_base_2d = PrettyTable()
    Aust_base_2d = PrettyTable()
    A_base_2d.title = ' Two day Change in Prices (USDT)'
    Aust_base_2d.title = ' Two day Change in Prices Australian Dollar  (USDT)'
    A_base_2d.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_base_2d.field_names= ["*****Symbol*****","*****priceChange*****", "****Start Price****", "****End Price****", "*****Percentage Change*****"]
        
    for s in sorted_list_base[:5]:
        A_base_2d.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_base_2d.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ************** End USTD Table 2 hour
    # ***************** For USDT as Base Coin (For 3 Day)
    base_list= []
    for base_index,  base_coin in enumerate(sorted_list_3d):
        if ( base_coin['symbol'].endswith('USDT')):
            temp_1= sorted_list_3d[base_index]
            base_list.append(temp_1)
    sorted_list_base=sorted(base_list, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # For USDT as Base Coin ******* Table
    A_base_3d = PrettyTable()
    Aust_base_3d = PrettyTable()
    A_base_3d.title = ' Three Days Change in Prices (USDT)'
    Aust_base_3d.title = ' Three Days Change in Prices Australian Dollar  (USDT)'
    A_base_3d.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_base_3d.field_names= ["*****Symbol*****","*****priceChange*****", "****Start Price****", "****End Price****", "*****Percentage Change*****"]
        
    for s in sorted_list_base[:5]:
        A_base_3d.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_base_3d.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ************** End USTD Table 4 hour
    # ***************** For USDT as Base Coin (For 5 day)
    base_list= []
    for base_index,  base_coin in enumerate(sorted_list_5d):
        if ( base_coin['symbol'].endswith('USDT')):
            temp_1= sorted_list_5d[base_index]
            base_list.append(temp_1)
    sorted_list_base=sorted(base_list, key=lambda x: abs(float(x['priceChange'])), reverse=True)
     # For USDT as Base Coin ******* Table
    A_base_5d = PrettyTable()
    Aust_base_5d = PrettyTable()
    A_base_5d.title = ' 5 Day Change in Prices (USDT)'
    Aust_base_5d.title = ' 5 Day Change in Prices Australian Dollar  (USDT)'
    A_base_5d.field_names= ["*****Symbol*****","*****priceChange*****", "*****Start Price*****", "*****End Price*****", "*****Percentage Change*****"]
    Aust_base_5d.field_names= ["*****Symbol*****","*****priceChange*****", "****Start Price****", "****End Price****", "*****Percentage Change*****"]
        
    for s in sorted_list_base[:5]:
        A_base_5d.add_row([s['symbol'],(float(s['priceChange'])) , s['openPrice'], s['lastPrice'], s['priceChangePercent']])
        Aust_base_5d.add_row([s['symbol'],(float(s['priceChange']))* aus_dollar , (float(s['openPrice']))*aus_dollar, (float(s['lastPrice']))*aus_dollar, s['priceChangePercent']])
    # ************** End USTD Table 8 hour

# ****************** Email For 1 Hour
    content=(str(A)+ str(Aust)+str(A_base)+str(Aust_base))
    msg = EmailMessage()
    msg['Subject'] = '1 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    msg.set_content(str(A)+ str(Aust)+str(A_base)+str(Aust_base))
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
# ********************** End Email 1 hour

# ****************** Email For 2 Hour
    content=(str(A_2h)+ str(Aust_2h)+str(A_base_2h)+str(Aust_base_2h))
    msg = EmailMessage()
    msg['Subject'] = ' 2 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    msg.set_content(str(A_2h)+ str(Aust_2h)+str(A_base_2h)+str(Aust_base_2h))
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
# ********************** End Email 2 hour

# ****************** Email For 4 Hour
    content=(str(A_4h)+ str(Aust_4h)+str(A_base_4h)+str(Aust_base_4h))
    msg = EmailMessage()
    msg['Subject'] = '4 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    msg.set_content(str(A_4h)+ str(Aust_4h)+str(A_base_4h)+str(Aust_base_4h))
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
# ********************** End Email 4 hour

# ****************** Email For 8 Hour
    content=(str(A_8h)+ str(Aust_8h)+str(A_base_8h)+str(Aust_base_8h))
    msg = EmailMessage()
    msg['Subject'] = '8 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    msg.set_content(str(A_8h)+ str(Aust_8h)+str(A_base_8h)+str(Aust_base_8h))
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
# ********************** End Email 8 hour
# ****************** Email For 24 Hour
    content=(str(A_24h)+ str(Aust_24h)+str(A_base_24h)+str(Aust_base_24h))
    msg = EmailMessage()
    msg['Subject'] = '24 Hour Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    msg.set_content(content)
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
# ********************** End Email 24 hour

# ****************** Email For 2 day
    content=(str(A_2d)+ str(Aust_2d)+str(A_base_2d)+str(Aust_base_2d))
    msg = EmailMessage()
    msg['Subject'] = ' Two Day Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    msg.set_content(str(A_2d)+ str(Aust_2d)+str(A_base_2d)+str(Aust_base_2d))
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
# ********************** End Email 2 day

# ****************** Email For 3 Day
    content=(str(A_3d)+ str(Aust_3d)+str(A_base_3d)+str(Aust_base_3d))
    msg = EmailMessage()
    msg['Subject'] = '3 Day Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    msg.set_content(str(A_3d)+ str(Aust_3d)+str(A_base_3d)+str(Aust_base_3d))
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
# ********************** End Email 3 day

# ****************** Email For 5 day
    content=(str(A_5d)+ str(Aust_5d)+str(A_base_5d)+str(Aust_base_5d))
    msg = EmailMessage()
    msg['Subject'] = '5 Day Roc of all coins'
    msg['To'] = 'tjjaccrypto@gmail.com'
    msg['From'] = 'kabocha608@gmail.com'
    msg.set_content(str(A_5d)+ str(Aust_5d)+str(A_base_5d)+str(Aust_base_5d))
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
# ********************** End Email 5 Day
   
    # print(A_base)
    # print(Aust_table)
    # last_price= r.json()1111
    index +=1
    print('******************************* End Loop *****************************')
    time.sleep(10)


