Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> x="salem"
>>> y="tamilnadu"
>>> mylist=["district","state",x,y]
>>> mylist
['district', 'state', 'salem', 'tamilnadu']
>>> mylist[1]
'state'
>>> mylist[2]
'salem'
>>> mylist[3]
'tamilnadu'
>>> mylist*2
['district', 'state', 'salem', 'tamilnadu', 'district', 'state', 'salem', 'tamilnadu']
>>> mylist[1:3]
['state', 'salem']
>>> mylist[::2]
['district', 'salem']
>>> mylist+mylist
['district', 'state', 'salem', 'tamilnadu', 'district', 'state', 'salem', 'tamilnadu']
>>> mylist
['district', 'state', 'salem', 'tamilnadu']
>>> mylist.count('salem')
1
>>> mylist.count('state')
1
>>> mylist.append('country')
>>> mylist
['district', 'state', 'salem', 'tamilnadu', 'country']
>>> mylist.remove('state')
>>> mylist
['district', 'salem', 'tamilnadu', 'country']
>>> mylist.insert(1,"state")
>>> mylist
['district', 'state', 'salem', 'tamilnadu', 'country']
>>> mylist.reverse()
>>> mylist
['country', 'tamilnadu', 'salem', 'state', 'district']
>>> mylist.reverse()
>>> mylist
['district', 'state', 'salem', 'tamilnadu', 'country']
>>> mylist.pop()
'country'
>>> mylist
['district', 'state', 'salem', 'tamilnadu']
>>> mylist.sort()
>>> mylist
['district', 'salem', 'state', 'tamilnadu']
>>> mylist.index('tamilnadu')
3
>>> a=[3,6,5,2,4,1]
>>> a.sort()
>>> print(a)
[1, 2, 3, 4, 5, 6]
>>> a=[3,6,5,2,4,1]
>>> a.sort(reverse=True)
>>> print(a)
[6, 5, 4, 3, 2, 1]
>>> a=[3,6,5,2,4,1]
>>> a.sort(reverse=False)
>>> print(a)
[1, 2, 3, 4, 5, 6]
>>> 
