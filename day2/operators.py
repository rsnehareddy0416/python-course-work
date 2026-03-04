Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=20
a+b
30
a-b
-10
a*b
200
a/b
0.5
a%b
10
a//b
0
b%10
0
9%2
1
a**2
100
b**3
8000
a=a+1
a
11
b+
SyntaxError: invalid syntax
b-=10
b
10
a+=10
a
21
a/=10
a
2.1
a==b
False
a!=b
True
a>b
False
b<a
False
a<b
True
a>10 and b<10
False
a>10 and b<10
False
a<10 and b<10
False
a>10 or b<10
False
a>10 or b>9
True
a<=b
True
not a/3==0
True
s="python"
'k' in s
False
't' in s
True
'n' in s
True
'y' not in s
False
'q' not in s
True
l=["komali","lavanya","lakshmi","madhavi"]
"komali" in l
True
"gowri" in l
False
"lavanya" not in l
False
t=(2,8,1,9)
2 in t
True
4 in t
False
8 not in t
False
s={"python","java","c"}
"python" in s
True
"html" in s
False
d={"python":"s1","java":"s2","html":"s3"}
s1 in d
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s1 in d
NameError: name 's1' is not defined. Did you mean: 's'?
>>> "s1" in d
False
>>> "python" in d
True
>>> "html" not in d
False
>>> a=[1,2,3,4]
>>> b=[1,2,3,4]
>>> a==b
True
>>> a is b
False
>>> c=a
>>> c
[1, 2, 3, 4]
>>> a==c
True
>>> id(a)
2127546660864
>>> id(b)
2127546754944
>>> id(c)
2127546660864
>>> c is not in b
SyntaxError: invalid syntax
>>> c is not b
True
>>> 6&7
6
>>> 7&8
0
>>> 7\9
SyntaxError: unexpected character after line continuation character
>>> 7|9
15
>>> 2>>3
0
>>> 4<<1
8
>>> 2>>1
1
>>> 16<<1
32
>>> 5>>1
2