Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
def is_factor(a, b):
    if b % a ==0:
        return True
    else:
        return False
... 
...     
>>> is_factor(4, 1024)
True
>>> for i in range(1, 4):
...     print(i)
... 
...     
1
2
3
>>> for i in range(5):
...     print(i)
... 
...     
0
1
2
3
4
>>> for i in range(1,10-2):
...     print(i)
... 
...     
1
2
3
4
5
6
7
>>> for i in range(1,10,2):
...     print i
...     
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> for i in range(1,10,2)
SyntaxError: expected ':'
>>> for i in range(1,10,2):
...     print(i)
... 
...     
1
3
5
7
9
