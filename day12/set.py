
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={1,2,3,4,5}
s[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[1:2]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[1:2]
TypeError: 'set' object is not subscriptable
s
{1, 2, 3, 4, 5}
s.add(1)
s.add(34.9)
s
{1, 2, 3, 4, 5, 34.9}
s.add("str")
s
{1, 2, 3, 4, 5, 34.9, 'str'}
s.add((1,2,3))
s
{1, 2, 3, 4, 5, 34.9, 'str', (1, 2, 3)}
s.add(3+8j)
s
{1, 2, 3, 4, 5, (3+8j), 34.9, (1, 2, 3), 'str'}
s.add(True)
s
{1, 2, 3, 4, 5, (3+8j), 34.9, (1, 2, 3), 'str'}
s.add(False)
s
{False, 1, 2, 3, 4, 5, (3+8j), 34.9, (1, 2, 3), 'str'}
s.add({1:6,9:7,9:6})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.add({1:6,9:7,9:6})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add({1,2,3})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s
{False, 1, 2, 3, 4, 5, (3+8j), 34.9, (1, 2, 3), 'str'}
s.add(8)
s
{False, 1, 2, 3, 4, 5, 8, (3+8j), 34.9, (1, 2, 3), 'str'}
s.pop(8)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.pop(8)
TypeError: set.pop() takes no arguments (1 given)
s.pop()
False
s.pop()
1
s.remove(4)
s
{2, 3, 5, 8, (3+8j), 34.9, (1, 2, 3), 'str'}
s.discard(5)
s
{2, 3, 8, (3+8j), 34.9, (1, 2, 3), 'str'}
s.clear()
s
set()
l=[]
t=()
d={}
s=set()
s
set()
{1,2}+{8,7}
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    {1,2}+{8,7}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
{1,2}*6
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    {1,2}*6
TypeError: unsupported operand type(s) for *: 'set' and 'int'
[1,2]*2
[1, 2, 1, 2]
s
set()
s={1,2,3,4,5}
2 in s
True
6 not in s
True
a={1,2,5,45,67,89}
a
{1, 2, 67, 5, 89, 45}
guys={"saaketh","swapnil","bharath"}
guys
{'swapnil', 'bharath', 'saaketh'}
girls={"komali","rishika","sneha"}
girls
{'rishika', 'komali', 'sneha'}
online={"komali","saaketh","poojitha","varsha"}
online
{'varsha', 'saaketh', 'komali', 'poojitha'}
guys.union(girls)
{'rishika', 'swapnil', 'bharath', 'saaketh', 'komali', 'sneha'}
girls | guys
{'rishika', 'swapnil', 'bharath', 'saaketh', 'komali', 'sneha'}
girls & guys
set()
online & guys
{'saaketh'}
online & girls
{'komali'}
girls.disjoint(online)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    girls.disjoint(online)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
girls.isdisjoint(online)
False
girls-online
{'rishika', 'sneha'}
girls^online
{'varsha', 'saaketh', 'rishika', 'poojitha', 'sneha'}
girls
{'rishika', 'komali', 'sneha'}
girls.update({"meghana","sanjana","sravanthi"})
girls
{'sanjana', 'rishika', 'sravanthi', 'meghana', 'komali', 'sneha'}
guys.update({"praveen","swapnil")
            
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
guys.update({"praveen","swapnil"})
            
guys
            
{'swapnil', 'bharath', 'saaketh', 'praveen'}
online()
            
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    online()
TypeError: 'set' object is not callable
online
            
{'varsha', 'saaketh', 'komali', 'poojitha'}
a={1,2,3,4,5,6,7,8}
            
b={7,8,9,10,12,11}
            
a.intersection(b)
            
{8, 7}
a.union(b)
            
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
a
            
{1, 2, 3, 4, 5, 6, 7, 8}
b
            
{7, 8, 9, 10, 11, 12}
a.intersection_update(9)
...             
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.intersection_update(9)
TypeError: 'int' object is not iterable
>>> a.intersection_update(b)
...             
>>> a
...             
{8, 7}
>>> s={1,2,3,4}
...             
>>> s
...             
{1, 2, 3, 4}
>>> {1,2}.issubset(s)
...             
True
>>> {8,9}.issubset(s)
...             
False
>>> s.issuperset({1,2,3,4})
...             
True
>>> {1,2,3,4}.issuperset(s)
...             
True
>>> max(a)
...             
8
>>> min(b)
...             
7
>>> id(a)
...             
1766170207936
>>> b=a
...             
>>> id(b)
...             
1766170207936
>>> c=a.copy()
...             
>>> c
...             
{8, 7}
