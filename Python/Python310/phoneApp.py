Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> 
>>> from twilio.rest import Client 
... 
... account_sid = 'ACCOUNT SID HERE' 
... auth_token = 'AUTH TOKEN HERE' 
... client = Client(account_sid, auth_token) 
... 
... message = client.messages.create(  
...     messaging_service_sid = 'MESSAGE SERVICE SID HERE',
...     body = 'WHATEVER YOU WANT TO SAY HERE',
...     to = '954-501-8419'
...     )
... 
