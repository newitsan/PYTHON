>>> class base:
	def method1(self):
		print('from base class')

	def method2(self,x,y):
		self.x=x
		self.y=y
		print("%s"  %  self.x,self.y)

		
>>> class derived(base):
	def method3(self):
		print('from derived class')

		
>>> obj=derived()
>>> obj.method1()
from base class
>>> obj.method2(10,20)
10 20
>>> obj.x=5
>>> obj.y=3
>>> obj.x
5
>>> obj.y
3
>>> getattr(obj,"x")
5
>>> getattr(obj,'y')
3
>>> hasattr(obj,'z')
False
>>> hasattr(obj,'x')
True
>>> setattr(obj,'x',7)
>>> getattr(obj,'x')
7
>>> delattr(obj,'y')

>>> hasattr(obj,'y')
False
>>> obj.y=4
>>> getattr(obj,'y')
4
