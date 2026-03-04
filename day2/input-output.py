Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=int(input("Enter the integer:"))
Enter the integer:21
a=float(input("Enter the float value:"))
Enter the float value:12.0
a
12.0
s=input("Enter string:")
Enter string:komali
s
'komali'
names=input("Enter names:")
Enter names:varsha sanjana meghana komali
names
'varsha sanjana meghana komali'
names.split
<built-in method split of str object at 0x000001369FE01E30>
names.split()
['varsha', 'sanjana', 'meghana', 'komali']
names.split(',')
['varsha sanjana meghana komali']
n='1,1,2,3'
n
'1,1,2,3'
n.split()
['1,1,2,3']
n.split(',')
['1', '1', '2', '3']
names=input("Enter the names:").split()
Enter the names:varsha sanjana meghana komali
names
['varsha', 'sanjana', 'meghana', 'komali']
rollno=input.split()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    rollno=input.split()
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
rollno=int(input("Enter no's:")).split()
Enter no's:1 2 4 8
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    rollno=int(input("Enter no's:")).split()
ValueError: invalid literal for int() with base 10: '1 2 4 8'
k=list(map(int,input().split()))
1 6 9 3 6 0 2
k
[1, 6, 9, 3, 6, 0, 2]
k=list(map(float,input().split()))
2 0 5 8 2 7
k
[2.0, 0.0, 5.0, 8.0, 2.0, 7.0]
k=input().split()
fgh iut awr
k
['fgh', 'iut', 'awr']
k=tuple(map(int,input().split()))
1 7 9 4
k
(1, 7, 9, 4)
k=list(map(float,input().split()))
2 9 3 5
k
[2.0, 9.0, 3.0, 5.0]
k=tuple(input().split())
34 98 05
k
('34', '98', '05')
k=set(map(int,input().split()))
34 667 09
k
{9, 34, 667}
k=list(map(float,input().split()))
34 09 56
k
[34.0, 9.0, 56.0]
k=set(input().split())
sdr kiu drty
k
{'drty', 'sdr', 'kiu'}
k=eval(input())
{12:"yui",56:"gty",09:"hyy"}
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    k=eval(input())
  File "<string>", line 1
    {12:"yui",56:"gty",09:"hyy"}
                       ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
k=eval(input())
{1:"awe1",2:"rty",3:"gty"}
k
{1: 'awe1', 2: 'rty', 3: 'gty'}
a,b,c=90,78,56
a
90
b
78
>>> c
56
>>> user_name,password=input().split()
komali@123
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    user_name,password=input().split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> user_name,password=input().split()
komali @123
>>> user_name
'komali'
>>> password
'@123'
>>> a=10
>>> b=13.0
>>> c="python"
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 13.0 c= python
>>> print("a=",a,"b=",b,"c=",c,sep="")
a=10b=13.0c=python
>>> print("a=",a,"b=",b,"c=",c,sep=" ")
a= 10 b= 13.0 c= python
>>> print(f"a={a} b={b} c={c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> SyntaxError: unterminated f-string literal (detected at line 1)
...       
SyntaxError: invalid syntax
>>> print(f"a={a} b={b} c={c}")
...       
a=10 b=13.0 c=python
>>> print(f"a=:{a},b=:{b},c=:{c}")
...       
a=:10,b=:13.0,c=:python
>>> print(f"a={a} \tb={b} \tc={c}
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"a={a}\tb={b}\tc={c}")
...       
a=10	b=13.0	c=python
>>> print(f"a={a}\nb={b}\nc={c}")
...       
a=10
b=13.0
c=python