Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
capitals = {"Florida": "Tallahassee", "Illinois": "Springfield", "Texas": "Austin", "Colorado": "Denver", "Wisconsin": "Madison", "North Carolina": "Raleigh", "Maine": "Augusta",}
a = capitals.get("Florida")
print(a)
Tallahassee
capitals.get(Texas)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    capitals.get(Texas)
NameError: name 'Texas' is not defined
a = capitals.get(Texas)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = capitals.get(Texas)
NameError: name 'Texas' is not defined
a = capitals.get(Texas)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a = capitals.get(Texas)
NameError: name 'Texas' is not defined
print(a)
Tallahassee
a = capitals.get("Texas")
print(a)
Austin
a
'Austin'
a
'Austin'
print(a)
Austin
b = capitals.get("Wisconsin")
>>> b
'Madison'
>>> print( a + " " b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(a + b)
AustinMadison
>>> capitals["Arizona"] "Phoenix"
SyntaxError: invalid syntax
>>> capitals["Arizona"] = "Phoenix"
>>> capitals
{'Florida': 'Tallahassee', 'Illinois': 'Springfield', 'Texas': 'Austin', 'Colorado': 'Denver', 'Wisconsin': 'Madison', 'North Carolina': 'Raleigh', 'Maine': 'Augusta', 'Arizona': 'Phoenix'}
>>> capitals["Montana"] = "Helena"
>>> capitals["Nevada"] = "Carson City"
>>> capitals["California"] = "Sacramento"
>>> capitals["Oregon"] = "Salem"
>>> capitals
{'Florida': 'Tallahassee', 'Illinois': 'Springfield', 'Texas': 'Austin', 'Colorado': 'Denver', 'Wisconsin': 'Madison', 'North Carolina': 'Raleigh', 'Maine': 'Augusta', 'Arizona': 'Phoenix', 'Montana': 'Helena', 'Nevada': 'Carson City', 'California': 'Sacramento', 'Oregon': 'Salem'}
>>> x = ('Florida', 'Colorado', 'Texas')
... y = 0
... 
... capitals = dict.fromkeys(x, y)
... 
... 
... print(capitals)
SyntaxError: multiple statements found while compiling a single statement
>>> x = ('Florida', 'Colorado', 'Texas')
>>> y = 0
>>> capitals = dict.fromkeys(x, y)
>>> print(capitals)
{'Florida': 0, 'Colorado': 0, 'Texas': 0}
>>> y = 5
>>> capitals = dict.fromkeys(x, y)
>>> print(capitals)
{'Florida': 5, 'Colorado': 5, 'Texas': 5}
