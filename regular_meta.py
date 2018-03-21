>>> import re
>>> x=re.findall(r"","i am new to python and i am going to learn datascience using python")
>>> print(x)
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
>>> x=re.findall(r"\w","i am new to python and i am going to learn datascience using python")
>>> print(x)
['i', 'a', 'm', 'n', 'e', 'w', 't', 'o', 'p', 'y', 't', 'h', 'o', 'n', 'a', 'n', 'd', 'i', 'a', 'm', 'g', 'o', 'i', 'n', 'g', 't', 'o', 'l', 'e', 'a', 'r', 'n', 'd', 'a', 't', 'a', 's', 'c', 'i', 'e', 'n', 'c', 'e', 'u', 's', 'i', 'n', 'g', 'p', 'y', 't', 'h', 'o', 'n']
>>> x=re.findall(r"\b\w","i am new to python and i am going to learn datascience using python")
>>> print(x)
['i', 'a', 'n', 't', 'p', 'a', 'i', 'a', 'g', 't', 'l', 'd', 'u', 'p']
>>> x=re.findall(r"\w\b","i am new to python and i am going to learn datascience using python")
>>> print(x)
['i', 'm', 'w', 'o', 'n', 'd', 'i', 'm', 'g', 'o', 'n', 'e', 'g', 'n']
>>> x=re.findall(r"\W","i am new to python and i am going to learn datascience using python")
>>> print(x)
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
>>> x=re.findall(r"\w*","i am new to python and i am going to learn datascience using python")
>>> print(x)
['i', '', 'am', '', 'new', '', 'to', '', 'python', '', 'and', '', 'i', '', 'am', '', 'going', '', 'to', '', 'learn', '', 'datascience', '', 'using', '', 'python', '']
>>> x=re.findall(r"\w+","i am new to python and i am going to learn datascience using python")
>>> print(x)
['i', 'am', 'new', 'to', 'python', 'and', 'i', 'am', 'going', 'to', 'learn', 'datascience', 'using', 'python']
>>> x=re.findall(r"\w$","i am new to python and i am going to learn datascience using python")
>>> print(x)
['n']
>>> x=re.findall(r"\b\b\w","i am new to python and i am going to learn datascience using python")
>>> print(x)
['i', 'a', 'n', 't', 'p', 'a', 'i', 'a', 'g', 't', 'l', 'd', 'u', 'p']
>>> x=re.findall(r"\+w","i am new to python and i am going to learn datascience using python")
>>> print(x)
[]
>>> x=re.findall(r"\$w","i am new to python and i am going to learn datascience using python")
>>> print(x)
[]
>>> x=re.findall(r"","i am new to python and i am going to learn datascience using python")
>>> print(x)
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
>>> x=re.findall(r"\b(4)","i am new to python and i am going to learn datascience using python")
>>> print(x)
[]
>>> x=re.findall(r"\w{3}","i am new to python and i am going to learn datascience using python")
>>> print(x)
['new', 'pyt', 'hon', 'and', 'goi', 'lea', 'dat', 'asc', 'ien', 'usi', 'pyt', 'hon']
>>> x=re.findall(r"\w{1-3}","i am new to python and i am going to learn datascience using python")
>>> print(x)
[]
>>> x=re.findall(r"\w{1,3}","i am new to python and i am going to learn datascience using python")
>>> print(x)
['i', 'am', 'new', 'to', 'pyt', 'hon', 'and', 'i', 'am', 'goi', 'ng', 'to', 'lea', 'rn', 'dat', 'asc', 'ien', 'ce', 'usi', 'ng', 'pyt', 'hon']
>>> x=re.findall(r"^\w","i am new to python and i am going to learn datascience using python")
>>> print(x)
['i']
>>> x=re.findall(r"^\W","i am new to python and i am going to learn datascience using python")
>>> print(x)
[]
>>> x=re.findall(r"^\B","i am new to python and i am going to learn datascience using python")
>>> print(x)
[]
>>> x=re.findall(r"^\b","i am new to python and i am going to learn datascience using python")
>>> print(x)
['']
>>> x=re.findall(r"^\w","i am new to python and i am going to learn datascience using python")
>>> print(x)
['i']
>>> x=re.findall(r"^\w$","i am new to python and i am going to learn datascience using python")
>>> print(x)
[]
>>> x=re.findall(r"\w$","i am new to python and i am going to learn datascience using python")
>>> print(x)
['n']
