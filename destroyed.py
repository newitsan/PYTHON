class sample:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		tot=(self.x+self.y)
		print(tot)
	def __del__(self):
		print("destroyed")
obj=sample(1,2)
a=obj
b=obj
del(obj)
del(a)
del(b)


