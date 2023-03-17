#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[38]:


#connect to website

URL = 'https://www.amazon.com/Eastshining-Adjustable-Microphone-Suspension-Microphones/dp/B076ZKGZ5X/ref=sr_1_13_sspa?crid=1JXIHXFAMDCGT&keywords=focusrite%2Bmic%2Barm&qid=1678979825&sprefix=focusrite%2Bmic%2Barm%2Caps%2C133&sr=8-13-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMEk3T1EwR1RCTEY3JmVuY3J5cHRlZElkPUEwMzQ4MTkyMkRSVklSRFhUT0xJTCZlbmNyeXB0ZWRBZElkPUEwMDM5OTk4MktXTVpGMzYwSUhVUiZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0", 
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.youtube.com/", 
    "Sec-Ch-Ua": "\"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"110\", \"Opera GX\";v=\"96\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find("span", class_ ='a-offscreen').get_text()

print(title)
print(price)


# In[39]:


title = title.strip()
price = price.strip()[1:]

print(title)
print(price)


# In[42]:


import datetime

today = datetime.date.today()

print(today)


# In[44]:


import csv

header = ['Title', 'Price', 'Date']
data = [title, price, today]

#with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
 #   writer = csv.writer(f)
  #  writer.writerow(header)
   # writer.writerow(data)





# In[41]:


import datetime

today = datetime.date.today()

print(today)


# In[46]:


import pandas as pd
df = pd.read_csv(r'C:\Users\jerem\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


#appending data

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[47]:


def check_price():
    URL = 'https://www.amazon.com/Eastshining-Adjustable-Microphone-Suspension-Microphones/dp/B076ZKGZ5X/ref=sr_1_13_sspa?crid=1JXIHXFAMDCGT&keywords=focusrite%2Bmic%2Barm&qid=1678979825&sprefix=focusrite%2Bmic%2Barm%2Caps%2C133&sr=8-13-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMEk3T1EwR1RCTEY3JmVuY3J5cHRlZElkPUEwMzQ4MTkyMkRSVklSRFhUT0xJTCZlbmNyeXB0ZWRBZElkPUEwMDM5OTk4MktXTVpGMzYwSUhVUiZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0", 
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
     "Accept-Encoding": "gzip, deflate, br", 
     "Accept-Language": "en-US,en;q=0.9",
     "Referer": "https://www.youtube.com/", 
     "Sec-Ch-Ua": "\"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"110\", \"Opera GX\";v=\"96\"", 
     "Sec-Ch-Ua-Mobile": "?0", 
     "Sec-Ch-Ua-Platform": "\"Windows\"", 
     "Sec-Fetch-Dest": "document", 
     "Sec-Fetch-Mode": "navigate", 
     "Sec-Fetch-Site": "cross-site", 
     "Sec-Fetch-User": "?1", 
     "Upgrade-Insecure-Requests": "1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find("span", class_ ='a-offscreen').get_text()
    
    title = title.strip()
    price = price.strip()[1:]
    import datetime

    today = datetime.date.today()
    
    import csv

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    if(price<17):
        send_mail()


# In[ ]:


#set timer to update data once a day
while(True)
    check_price()
    time.sleep(86400)


# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('jeremyjerrific@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "This item is now at your desired price"
    body = "Hey Jeremy, that thing you wanted is now below $17. Jump on this before it's too late!"
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'AlexTheAnalyst95@gmail.com',
        msg
     
    )


# In[ ]:





# In[ ]:





# In[ ]:




