>>> dict={"name":"santhosh","age":21,"place":"salem"}
>>> dict
{'place': 'salem', 'age': 21, 'name': 'santhosh'}
>>> dict["name"]
'santhosh'
>>> dict["age"]
21
>>> dict["place"]
'salem'
>>> dict.keys()
dict_keys(['place', 'age', 'name'])
>>> dict.values()
dict_values(['salem', 21, 'santhosh'])
>>> dict1=dict.copy()
>>> dict1
{'place': 'salem', 'age': 21, 'name': 'santhosh'}
>>> x=dict()
>>> x=dict
>>> dict1.clear()
>>> dict1
{}
>>> x.clear()
>>> x
{}
>>> dict
{}
>>> dict={"name":"santhosh","age":21,"place":"salem"}
>>> dict
{'place': 'salem', 'age': 21, 'name': 'santhosh'}
>>> dict.get("name")
'santhosh'
>>> dict.get("age")
21
>>> dict.get("place")
'salem'
>>> dict.pop('name')
'santhosh'
>>> dict
{'place': 'salem', 'age': 21}
>>> dict.pop("age")
21
>>> dict
{'place': 'salem'}
>>> dict.pop('place')
'salem'
>>> dict
{}
>>> dict={"name":"santhosh","age":21,"place":"salem"}
>>> dict.popitems()
>>> dict.popitem()
('place', 'salem')
>>> dict.popitem()
('age', 21)
>>> dict.popitem()
('name', 'santhosh')
>>> dict
{}
>>> dict={"name":"santhosh","age":21,"place":"salem"}
>>> dict
{'place': 'salem', 'age': 21, 'name': 'santhosh'}
>>> dict['address']='t-nagar'
>>> dict
{'place': 'salem', 'address': 't-nagar', 'age': 21, 'name': 'santhosh'}
>>> dict.pop("address")
't-nagar'
>>> dict
{'place': 'salem', 'age': 21, 'name': 'santhosh'}
>>> dict.update({"address":"t-nagar"})
>>> dict
{'place': 'salem', 'address': 't-nagar', 'age': 21, 'name': 'santhosh'}
>>> dict.pop("address")
't-nagar'
>>> dict
{'place': 'salem', 'age': 21, 'name': 'santhosh'}
>>> dict.update({"address":"t-nager","pin":600001})
>>> dict
{'address': 't-nager', 'age': 21, 'place': 'salem', 'pin': 600001, 'name': 'santhosh'}
>>> d1={"state":"tamilnadu"}
>>> dict.update(d1)
>>> dict
{'address': 't-nager', 'age': 21, 'place': 'salem', 'state': 'tamilnadu', 'pin': 600001, 'name': 'santhosh'}
>>> student={1:{address': 't-nager', 'age': 21, 'place': 'salem', 'state': 'tamilnadu', 'pin': 600001, 'name': 'santhosh'}}

>>> for i in sys.path:
	print(i)

	

/home/i18n
/usr/bin
/usr/lib/python35.zip
/usr/lib/python3.5
/usr/lib/python3.5/plat-x86_64-linux-gnu
/usr/lib/python3.5/lib-dynload
/usr/local/lib/python3.5/dist-packages
/usr/lib/python3/dist-packages
>>> 
