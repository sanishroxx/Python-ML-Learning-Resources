Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hour=24
>>> 
================================ RESTART: Shell ================================
>>> minutes=60
>>> hours=24
>>> days=7
>>> print("minutes in per day")
minutes in per day
>>> print(mintues*hours)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(mintues*hours)
NameError: name 'mintues' is not defined
>>> print(minutes*hours)
1440
>>> print("hours in week")
hours in week
>>> print(hours*days)
168
>>> 