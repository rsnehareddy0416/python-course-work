Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
'*'*50
'**************************************************'
names='sirishavarshakomalidivya'
names[0]
's'
names[-1]
'a'
names[8]
'a'
names[0:7:1]
'sirisha'
names[7:13]
'varsha'
names[13:19]
'komali'
names[-1:-6]
''
names[-1:6]
''
names[19:]
'divya'
names[::-1]
'ayvidilamokahsravahsiris'
names
'sirishavarshakomalidivya'
names[-7:-1]
'lidivy'
names[-7::-1]
'lamokahsravahsiris'
names
'sirishavarshakomalidivya'
names[7::-1]
'vahsiris'
names[6::-1]
'ahsiris'
names[-1:5]
''
names[12:6:-1]
'ahsrav'
names[18:6:-1]
'ilamokahsrav'
names[18:12:-1]
'ilamok'
names[19:-1]
'divy'
names[19:1]
''
names[-5:]
'divya'
list=[KomaliLavanyaMadhaviLakshmi]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list=[KomaliLavanyaMadhaviLakshmi]
NameError: name 'KomaliLavanyaMadhaviLakshmi' is not defined
list='KomaliLavanyaMadhaviLakshmi'
list[0]
'K'
list[-1]
'i'
list[6]
'L'
list[::-1]
'imhskaLivahdaMaynavaLilamoK'
list[0:6:1]
'Komali'
list[5:1:-1]
'ilam'
list[6:1:-1]
'Lilam'
list[5::-1]
'ilamoK'
list[6:13:1]
'Lavanya'
list[12:7:-1]
'aynav'
list[12:6:-1]
'aynava'
list[12:7:-1]
'aynav'
list[12:5:-1]
'aynavaL'
list[13:20:1]
'Madhavi'
list[12:19:-1]
''
list[19:12:-1]
'ivahdaM'
list[20:]
'Lakshmi'
list[20:27]
'Lakshmi'
list[26:19:-1]
'imhskaL'
list[-7:]
'Lakshmi'
names
'sirishavarshakomalidivya'
'Komali' in names
False
'komali' in names
True
'satwik' in names
False
len(names)
24
max(names)
'y'
min(names)
'a'
ord('a')
97
ord('A')
65
ord('z')
122
ch(60)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    ch(60)
NameError: name 'ch' is not defined. Did you mean: 'chr'?
chr(60)
'<'
chr(97)
'a'
chr(5)
'\x05'
chr(30)
'\x1e'
sorted(names)
['a', 'a', 'a', 'a', 'a', 'd', 'h', 'h', 'i', 'i', 'i', 'i', 'k', 'l', 'm', 'o', 'r', 'r', 's', 's', 's', 'v', 'v', 'y']
list
'KomaliLavanyaMadhaviLakshmi'
list.isupper()
False
list.upper()
'KOMALILAVANYAMADHAVILAKSHMI'
list.lower()
'komalilavanyamadhavilakshmi'
list.swapcase()
'kOMALIlAVANYAmADHAVIlAKSHMI'
list.isalpha()
True
list.isdigit()
False
list.isalnum()
True
a="python"
a.center(30,'-')
'------------python------------'
a.ljust(30,'-')
'python------------------------'
a.rjust(30,'-')
'------------------------python'
'python.pp' .startswith('p')
True
'python.py' .endswith('y')
True
s="python is easy"
s.replace('python','java')
'java is easy'
s
'python is easy'
s.title()
'Python Is Easy'
s.captilize()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
>>> s.captilize()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
>>> s.capitalize()
'Python is easy'
>>> s.strip()
'python is easy'
>>> s.lstrip()
'python is easy'
>>> s.rstrip()
'python is easy'
>>> s='     python     '
>>> s=
SyntaxError: invalid syntax
>>> s.strip()
'python'
>>> s.lstrip()
'python     '
>>> s.rstrip()
'     python'
>>> s.index('y')
6
>>> s.index('p')
5
>>> s="pyhon is easy"
>>> s.index(0)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s.index(0)
TypeError: index() argument 1 must be str, not int
>>> s
'pyhon is easy'
>>> s.index('p')
0
>>> s.index('y')
1
>>> s.find('e')
9
>>> s.find('t')
-1