Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def getQuantity(A,B):
...     amount = A + B
...     print("The total amount is {}".format(amount))
... 
...     
>>>     getQuantity(527,4)
...     
SyntaxError: unexpected indent
>>> def getQuantity(A,B):
...     amount = A + B
...     print("The total amount is {}".format(amount))
... 
...     
... getQuantity(527,4)
SyntaxError: invalid syntax
>>> def getQuantity(A,B):
...     amount = A * B
...     print("The total amount is {}".format(amount))
... 
...     
...     getQuantity(527,4)
... 
...     
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def getQuantity(A,B):
...     amount = A / B
...     print("The total amount is {}".format(amount))
... 
...     