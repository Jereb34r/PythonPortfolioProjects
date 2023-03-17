#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'a54c2094-cd5e-439f-8df6-d316bf6c5c02',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[2]:


type(data)


# In[22]:


import pandas as pd

pd.set_option('display.max_columns', None)


# In[8]:


df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df


# In[ ]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'5000',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'a54c2094-cd5e-439f-8df6-d316bf6c5c02',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    #df2 = pd.json_normalize(data['data'])
    #df2['timestamp'] = pd.to_datetime('now')
    #df = df.append(df2)
    
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df
    
    if not os.path.isfile(r'C:\Users\jerem\Documents\PythonAPIScripts\API.csv'):
        df.to_csv(r'C:\Users\jerem\Documents\PythonAPIScripts\API.csv', header = 'column_names')
    else:
        df.to_csv(r'C:\Users\jerem\Documents\PythonAPIScripts\API.csv', mode='a', header=FALSE)


# In[ ]:


import os
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print("Run was successful")
    sleep(60)
exit()


# In[33]:


if not os.path.isfile(r'C:\Users\jerem\Documents\PythonAPIScripts\API.csv'):
        df.to_csv(r'C:\Users\jerem\Documents\PythonAPIScripts\API.csv', header = 'column_names')
else:
        df.to_csv(r'C:\Users\jerem\Documents\PythonAPIScripts\API.csv', mode='a', header=FALSE)


# In[34]:


df3 = pd.read_csv(r'C:\Users\jerem\Documents\PythonAPIScripts\API.csv')
df3


# In[35]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[36]:


df3 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df3


# In[37]:


df4 = df3.stack()
df4


# In[43]:


df5=df4.to_frame(name='values')
df5


# In[52]:


df5.count()


# In[78]:


df5_sub = df5.head(50)#table with small subset of data to make loading the plot easier
df5_sub


# In[79]:



index = pd.Index(range(50)) 

df6 = df5_sub.set_index(index)
df6 = df5_sub.reset_index()
df6


# In[80]:


df7 = df6.rename(columns={'level_1': 'percent_change'})
df7


# In[81]:


df7['percent_change'] = df7['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
df7


# In[82]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[91]:


sns.catplot(x='percent_change', y='values', hue='name', data=df7, kind='point')
plt.show()


# In[94]:


df8 = df[['name', 'quote.USD.price', 'timestamp']]
df8 = df8.query("name=='Bitcoin'")
df8


# In[105]:


df8 = df8.reset_index()
df8


# In[109]:


sns.set_theme(style="darkgrid")
plot_ = sns.lineplot(x='timestamp', y='quote.USD.price', data=df8)
plot_.xaxis.set_major_locator(plt.LinearLocator(5))
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




