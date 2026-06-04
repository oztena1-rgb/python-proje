Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=input()
1
a
'1'
s1='a string'
>>> s2="a string"
>>> a="1"
>>> int(a)+1
2
>>> float(a)+1
2.0
>>> int('2')
2
>>> int('2.0')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int('2.0')
ValueError: invalid literal for int() with base 10: '2.0'
>>> a=float(input())
3/4
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a=float(input())
ValueError: could not convert string to float: '3/4'
>>> try:
...     a=float(input('Enter a number: '))
...     3/4
... 3/4
SyntaxError: expected 'except' or 'finally' block
>>> a=input('Input an integer: ')
Input an integer: 1
>>> a=int(input())
a+1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: 'a+1'
>>> a=int(input())
1
>>> a
1
>>> a+1
2
>>> a=int(input())
1.0
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: '1.0'
>>> 1.0.is_integer()
True
