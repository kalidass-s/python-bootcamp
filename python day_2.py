Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30days 30 hours")
30days 30 hours
>>> hours = "thirty"
>>> print(hours)
thirty
>>> print(hours[0])
t
>>> challenge = "i will win"
>>> print(challenge[7:10])
win
>>> print(challenge[1:10])
 will win
>>> print(challenge[0:10])
i will win
>>> print(len(challenege))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(len(challenege))
NameError: name 'challenege' is not defined
>>> print(len(challenge))
10
>>> a=30
>>> b=30
>>> c =a-b
>>> print(c)
0
>>> c=a+""+b
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c=a+""+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> c=a+ " " +b
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c=a+ " " +b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> text="thirty days and thirty hours"
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> y=text.capitalize()
>>> print(y)
Thirty days and thirty hours
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> z=text.find()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    z=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> print(challenge.upper())
I WILL WIN
>>> z=text.find("days")
>>> print(z)
7
>>> k=text.isalpha()
>>> print(k)
False
>>> n=text.isalnum()
>>> print(n)
False
>>> d=a+" "+b
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d=a+" "+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a="3  hours"
>>> b="3  days"
>>> c=a+" "+b
>>> print(c)
3  hours 3  days
>>> 