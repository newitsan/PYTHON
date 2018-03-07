Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> l1=[1,2,3,4,5,6,7,8,9,10]
>>> l1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l2=["santhosh","priya","migen"]
>>> l2
['santhosh', 'priya', 'migen']
>>> l1=[l1 for i in range of (0,10)]
SyntaxError: invalid syntax
>>> l1=[l1 for i in range  (0,10)]
>>> l1
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
>>> l2.append["dharmapuri"]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l2.append["dharmapuri"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l2.append("dharmapuri")
>>> l2
['santhosh', 'priya', 'migen', 'dharmapuri']
>>> del(l1)
>>> l1
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l1
NameError: name 'l1' is not defined
>>> l1=[1,2,3,4,5,6,7,8,9,10]
>>> l1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l2
['santhosh', 'priya', 'migen', 'dharmapuri']
>>> del(l2(3))
SyntaxError: can't delete function call
>>> del(l2[3])
>>> l2
['santhosh', 'priya', 'migen']
>>> l1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> del(l1[0])
>>> l1
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l1.append(1)
>>> l1
[2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
>>> min(l1)
1
>>> max(l1)
10
>>> lis=[]
>>> for i in range(0,10)
SyntaxError: invalid syntax
>>> lis=[]for i in range(0,10):
	
SyntaxError: invalid syntax
>>> lis=[]for i in range(0,10):
	
SyntaxError: invalid syntax
>>> lis=[]
>>> for i in range(0,10):
	lis.append(i)

	
>>> lis
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for l1 in range (0,10,2):
	l1.append(i)

	
Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    l1.append(i)
AttributeError: 'int' object has no attribute 'append'
>>> lis[]
SyntaxError: invalid syntax
>>> lis=[]
>>> for i in range(0,10,2)
SyntaxError: invalid syntax
>>> lis=[]for i in range(0,10,2):
	
SyntaxError: invalid syntax
>>> lis=[]
>>> for i in range(0,10,2):
	lis.append(i)

	
>>> lis
[0, 2, 4, 6, 8]
>>> l1=[l1*2 for i in range(0,10)]
>>> l1
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> l1=[1,2,3,4,5,6,7,8,9,10]
>>> l1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l1=[l1*2 for i in range(0,10)]
>>> l1
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
>>> l1=[1,2,3,4,5,6,7,8,9,10]
>>> l1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l1[0:9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l1[::2]
[1, 3, 5, 7, 9]
>>> l1[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
