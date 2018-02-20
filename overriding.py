Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # though the structure of program looks like overriding but it is not overriding, it is evident from their memory location.
>>> 
>>> class student:
	def display(self,x):
		self.x=x
		print(self.x)

		
>>> class base(student):
	def display(self,x):
		self.x=x
		print(self.x)

>>> obj=student()
>>> obj.display(1)
1
>>> obj1=base()
>>> obj.display(1)
1
>>> student.__dict__
mappingproxy({'display': <function student.display at 0x7f94b7497378>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'student' objects>, '__doc__': None, '__weakref__': <attribute '__weakref__' of 'student' objects>})
>>> base.__dict__
mappingproxy({'display': <function base.display at 0x7f94b136e488>, '__module__': '__main__', '__doc__': None})
>>> 
