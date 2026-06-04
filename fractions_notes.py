Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from fractions import Fraction
>>> f=Fraction(3,4)
>>> f
Fraction(3, 4)
>>> Fraction(3,4)+1+1.5
3.25
>>> Fraction(3,4)+1+Fraction(1/4)
Fraction(2, 1)
>>> a=2+3j
>>> type(a)
<class 'complex'>
>>> a=complex(2,3)
>>> a
(2+3j)
>>> b=3+3j
>>> a+b
(5+6j)
>>> a-b
(-1+0j)
>>> a*b
(-3+15j)
>>> a/b
(0.8333333333333334+0.16666666666666666j)
>>> z=2+3j
>>> z.real
2.0
>>> z,imag
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    z,imag
NameError: name 'imag' is not defined
>>> z.imag
3.0
>>> z.conjugate()
(2-3j)
>>> (z.real**2+z.imag**2)**0.5
3.605551275463989
