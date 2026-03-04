Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
myvar=90
Myvar=09
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
Myvar=12
myvar@=67
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    myvar@=67
TypeError: unsupported operand type(s) for @=: 'int' and 'int'
My=11
1myvar=87
SyntaxError: invalid decimal literal
_myvar=11
if=67
SyntaxError: invalid syntax
m=12
m=23
M=12
m
23
M
12
a=10
b=10.8
c=12.9j
type(a)
<class 'int'>
type(b)
<class 'float'>
type(c)
<class 'complex'>
s="python"
s='python'
s='''python'''
s="""python"""
s='"python"'
type(s)
<class 'str'>
s
'"python"'
s='python'
s
'python'
id(s)
2449665801888
s=s+"lang"
s
'pythonlang'
id(s)
2449710027120
s
'pythonlang'
l=["sunset.png","moun.mp4","sunr.png","sunr.png"]
l
['sunset.png', 'moun.mp4', 'sunr.png', 'sunr.png']
id(l)
2449709970880
l.append("beach.mp4")
l
['sunset.png', 'moun.mp4', 'sunr.png', 'sunr.png', 'beach.mp4']
id(l)
2449709970880
l[0]
'sunset.png'
l[3]
'sunr.png'
l
['sunset.png', 'moun.mp4', 'sunr.png', 'sunr.png', 'beach.mp4']
id(1)
140724398879864
type(l)
<class 'list'>
t=('sunset.png', 'moun.mp4', 'sunr.png', 'sunr.png')
t
('sunset.png', 'moun.mp4', 'sunr.png', 'sunr.png')
type(t)
<class 'tuple'>
id(t)
2449710093456
s={"komali","lavanya","lakshmi","madhavi"}
type(s)
<class 'set'>
s.add("karuna")
s
{'madhavi', 'lavanya', 'komali', 'lakshmi', 'karuna'}
s.append("varsha")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s.append("varsha")
AttributeError: 'set' object has no attribute 'append'
s.add(varsha)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s.add(varsha)
NameError: name 'varsha' is not defined. Did you mean: 'vars'?
s.add("varsha")
s
{'madhavi', 'lavanya', 'komali', 'varsha', 'lakshmi', 'karuna'}
id(s)
2449709636896
data={}
data={"name":"komali","regno":"210","course":"PFS"}
data
{'name': 'komali', 'regno': '210', 'course': 'PFS'}
type(data)
<class 'dict'>
data['name']="Lavanya"
data
{'name': 'Lavanya', 'regno': '210', 'course': 'PFS'}
data['Skills']=["py","html","js"]
data
{'name': 'Lavanya', 'regno': '210', 'course': 'PFS', 'Skills': ['py', 'html', 'js']}
id(data)
2449710027520
payment_status=False
type(payment_status)
<class 'bool'>
a=True
type(a)
<class 'bool'>
a=''
a=0
a=None
a

==================================================================== RESTART: C:/Users/DELL/OneDrive/Desktop/day1.py ===================================================================
Enter a product:lenova
Enter the stock:10
Enter price:50000
>>> 
==================================================================== RESTART: C:/Users/DELL/OneDrive/Desktop/day1.py ===================================================================
Enter a product:lenova
Enter the stock:23
Enter price:50000
Enter the avail sizes:[6,8,12]
Enter the reviews:["good","worst","better"]
Enter the payment_modes:upi
Traceback (most recent call last):
  File "C:/Users/DELL/OneDrive/Desktop/day1.py", line 7, in <module>
    payment_mode=eval(input("Enter the payment_modes:"))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'upi' is not defined
>>> 
>>> 
==================================================================== RESTART: C:/Users/DELL/OneDrive/Desktop/day1.py ===================================================================
Enter a product:lenova
Enter the stock:20
Enter price:50000
Enter the avail sizes:[6,8,12]
Enter the reviews:["worst","good"'"better"]
Traceback (most recent call last):
  File "C:/Users/DELL/OneDrive/Desktop/day1.py", line 6, in <module>
    reviews=eval(input("Enter the reviews:"))
  File "<string>", line 1
    ["worst","good"'"better"]
                   ^
SyntaxError: unterminated string literal (detected at line 1)
>>> 
==================================================================== RESTART: C:/Users/DELL/OneDrive/Desktop/day1.py ===================================================================
Enter a product:lenova
Enter the stock:20
Enter price:50000
Enter the avail sizes:[6,8,12]
Enter the reviews:["worst","good","better"]
Enter the payment_modes:("COD","UPI","CARDS")
Enter the brand details:{"screen size":"12.7","colour":"black"}
product_name:lenova
stock:20
price:50000.0
RAM:[6, 8, 12]
reviews:['worst', 'good', 'better']
payment_mode:('COD', 'UPI', 'CARDS')
brand:{'screen size': '12.7', 'colour': 'black'}