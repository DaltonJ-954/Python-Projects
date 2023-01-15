Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tools = {"screws", "happer", "ruler"}
tools.add("wrench")
tools
{'screws', 'wrench', 'happer', 'ruler'}
tools.remove("happer")
>>> tools.add("hammer")
>>> tools
{'ruler', 'hammer', 'wrench', 'screws'}
>>> tools.difference()
{'screws', 'hammer', 'wrench', 'ruler'}
>>> myDictionary = {'index1': 1,'index2': 2,'index3': 355}
>>> myDictionary
{'index1': 1, 'index2': 2, 'index3': 355}
>>> myDictionary['index2']
2
>>> myDictionary['index3']
355
>>> dic_users = {'em_12234': {'fname': 'Sergio', 'lname': 'Walls',}}
>>>  dic_users = {'em_12234': {'fname': 'bob', 'lname': 'smith', 'phone': '561-553-0912'}, 'em_12235': {'fname': 'sylvia', 'lname': 'mccloud', 'phone': '561-332-5674'} }
...  
SyntaxError: unexpected indent
>>> dic_users = {'em_12234': {'fname': 'bob', 'lname': 'smith', 'phone': '561-553-0912'}, 'em_12235': {'fname': 'sylvia', 'lname': 'mccloud', 'phone': '561-332-5674'}}
>>> dic_users
{'em_12234': {'fname': 'bob', 'lname': 'smith', 'phone': '561-553-0912'}, 'em_12235': {'fname': 'sylvia', 'lname': 'mccloud', 'phone': '561-332-5674'}}
>>> print(dic_users[em_12235])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(dic_users[em_12235])
NameError: name 'em_12235' is not defined
>>> print(dic_users['em_12235]')
...       
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(dic_users['em_12235'])
...       
{'fname': 'sylvia', 'lname': 'mccloud', 'phone': '561-332-5674'}
>>> print(dic_users['em_12235']['phone'])
...       
561-332-5674
>>> print('User: {} ()\nPhone: {}'.format(dic_users['em_12235']['fname'],dic_users['em_12235']['lname'],dic_users['em_12235']['phone'])







print('User: {} ()\nPhone: {}'.format(dic_users['em_12235']['fname'],dic_users['em_12235']['lname'],dic_users['em_12235']['phone'])
      
SyntaxError: '(' was never closed



print('User: {} ()\nPhone: {}'.format(dic_users['em_12235']['fname'],dic_users['em_12235']['lname'],dic_users['em_12235']['phone']))
      
User: sylvia ()
Phone: mccloud
print('User: {} {}\nPhone: {}'.format(dic_users['em_12235']['fname'],dic_users['em_12235']['lname'],dic_users['em_12235']['phone']))
      
User: sylvia mccloud
Phone: 561-332-5674
