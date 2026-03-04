Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
float(a)
10.0
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=12.9
int(a)
10
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c="string"
int(c)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: 'string'
type(c)
<class 'str'>
type(b)
<class 'float'>
type(a)
<class 'int'>
float(a)
10.0
list(c)
['s', 't', 'r', 'i', 'n', 'g']
tuple(c)
('s', 't', 'r', 'i', 'n', 'g')
set(c)
{'n', 's', 'r', 'g', 't', 'i'}
dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(c)
True
s="123"
int(s)
123
float(s)
123.0
str(s)
'123'
list(s)
['1', '2', '3']
tuple(s)
('1', '2', '3')
set{s}
SyntaxError: invalid syntax
set(s)
{'2', '1', '3'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
l=[1,2,4,6]
int(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)]
SyntaxError: unmatched ']'
str(l)
'[1, 2, 4, 6]'
tuple(l)
(1, 2, 4, 6)
set(l)
{1, 2, 4, 6}
dict(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> t=(1,3,5,9)
>>> list(t)
[1, 3, 5, 9]
>>> set(t)
{1, 3, 5, 9}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
True
>>> s={1,3,8,2,}
>>> list(s)
[8, 1, 2, 3]
>>> tuple(s)
(8, 1, 2, 3)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> d={"name":"komali","rollno":210}
>>> d
{'name': 'komali', 'rollno': 210}
>>> list(d)
['name', 'rollno']
>>> set(d)
{'rollno', 'name'}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> str(d)
"{'name': 'komali', 'rollno': 210}"
>>> tuple(d)
('name', 'rollno')
>>> bool(d)
True
>>> complex(a)
(10+0j)