Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={"komali":19,"sneha":16,"rishika":15,"varsha":11,"bhavana":9}
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 11, 'bhavana': 9}
d.keys()
dict_keys(['komali', 'sneha', 'rishika', 'varsha', 'bhavana'])
d.values()
dict_values([19, 16, 15, 11, 9])
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 11, 'bhavana': 9}
d.items()
dict_items([('komali', 19), ('sneha', 16), ('rishika', 15), ('varsha', 11), ('bhavana', 9)])
e={}
e=dict()
e
{}
d['saaketh']
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d['saaketh']
KeyError: 'saaketh'
d['sneha']
16
d['komali']
19
d.get('sravanthi')
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 11, 'bhavana': 9}
d.get('komali')
19
d.get('sravanthi',"name is not present")
'name is not present'
d.get('komali',"name is not present")
19
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 11, 'bhavana': 9}
d['rishika']
15
id(d)
2643432803968
d['varsha']=18
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 18, 'bhavana': 9}
d['sajitha']=12
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 18, 'bhavana': 9, 'sajitha': 12}
d['bhanu']=13
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 18, 'bhavana': 9, 'sajitha': 12, 'bhanu': 13}
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 18, 'bhavana': 9, 'sajitha': 12, 'bhanu': 13}
d.update({"raji":0,"pavi":14})
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 18, 'bhavana': 9, 'sajitha': 12, 'bhanu': 13, 'raji': 0, 'pavi': 14}
d.pop('pavi')
14
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 18, 'bhavana': 9, 'sajitha': 12, 'bhanu': 13, 'raji': 0}
d.popitem()
('raji', 0)
d.popitem()
('bhanu', 13)
d.popitem()
('sajitha', 12)
d
{'komali': 19, 'sneha': 16, 'rishika': 15, 'varsha': 18, 'bhavana': 9}
del d['rishika']
d
{'komali': 19, 'sneha': 16, 'varsha': 18, 'bhavana': 9}
d.clear()
d
{}
d={"preveen":12,"satwik":15}
d.get('sakeeth')
d
{'preveen': 12, 'satwik': 15}
d.get('sakeeth':12)
SyntaxError: invalid syntax
d.setdefault('sakeeth',0)
0
d
{'preveen': 12, 'satwik': 15, 'sakeeth': 0}
d.set.default('praveen',0)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d.set.default('praveen',0)
AttributeError: 'dict' object has no attribute 'set'. Did you mean: 'get'?
d.setdefault('praveen',0)
0
d
{'preveen': 12, 'satwik': 15, 'sakeeth': 0, 'praveen': 0}
d.clear()
d
{}
d[1]='int'
d
{1: 'int'}
d[2.6]='float'
d
{1: 'int', 2.6: 'float'}
d[str]='string'
d
{1: 'int', 2.6: 'float', <class 'str'>: 'string'}
d['string']='string'
d
{1: 'int', 2.6: 'float', <class 'str'>: 'string', 'string': 'string'}
>>> d[2+4j]='complex'
>>> d
{1: 'int', 2.6: 'float', <class 'str'>: 'string', 'string': 'string', (2+4j): 'complex'}
>>> d[1,2,3]='list'
>>> d
{1: 'int', 2.6: 'float', <class 'str'>: 'string', 'string': 'string', (2+4j): 'complex', (1, 2, 3): 'list'}
>>> d(1,2,3)='tuple'
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
>>> d[(1,2,3)]='tuple'
>>> d
{1: 'int', 2.6: 'float', <class 'str'>: 'string', 'string': 'string', (2+4j): 'complex', (1, 2, 3): 'tuple'}
>>> d[{1,2,3}]='set'
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d[{1,2,3}]='set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
>>> d
{1: 'int', 2.6: 'float', <class 'str'>: 'string', 'string': 'string', (2+4j): 'complex', (1, 2, 3): 'tuple'}
>>> d[{1:1,2:4}]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    d[{1:1,2:4}]
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
>>> d
{1: 'int', 2.6: 'float', <class 'str'>: 'string', 'string': 'string', (2+4j): 'complex', (1, 2, 3): 'tuple'}
>>> d.clear()
>>> d
{}
>>> d['var1']=1
>>> d
{'var1': 1}
>>> d['var2']=2
>>> d
{'var1': 1, 'var2': 2}
>>> d['var3']='srt'
>>> d
{'var1': 1, 'var2': 2, 'var3': 'srt'}
>>> d['var2']=[1,2,3,4]
>>> d
{'var1': 1, 'var2': [1, 2, 3, 4], 'var3': 'srt'}