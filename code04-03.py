Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=ord('A')
>>> mask=0x0F
>>> 
>>> print("%x & %x = %x" % (a, mask, a & mask))
41 & f = 1
>>> print("%X & %X = %X" % (a, mask, a   mask))
SyntaxError: invalid syntax
>>> print("%X & %X = %X" % (a, mask, a | mask))
41 & F = 4F
>>> 
>>> mask=ord('a') - ard('A')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    mask=ord('a') - ard('A')
NameError: name 'ard' is not defined
>>> mask = ord('a') - ard('A')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    mask = ord('a') - ard('A')
NameError: name 'ard' is not defined
>>> a = ord('A')
>>> mask = 0x0F
>>> 
>>> print("%x & %x = %x" % (a, mask, a & mask))
41 & f = 1
>>> print("%X & %X = %X" % (a, mask, a | mask))
41 & F = 4F
>>> 
>>> mask = ord('a')-ord('A')
>>> 
>>> b = a^mask
>>> print("%c ^ %d = %c" % (a, mask, b))
A ^ 32 = a
>>> a = b^mask
>>> print("%c ^ %d = %c" % (b, mask, a))
 a ^ 32 = A
>>> 
