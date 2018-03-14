>>> f=open("simple.txt","w")
>>> f.write("i am new to python")
18
>>> f.close()
>>> f=open("simple.txt")
>>> f.readline()
'i am new to python'
>>> f=open("simple.txt","a")
>>> f.write(  "but python is an intresting language.")
37
>>> f=open("simple.txt")
>>> f.readline()
'i am new to pythonbut python is an intresting language.'
>>> f.closed
False
>>> f.open
>>> with open("simple.txt","w") as f:
	f.write("JAVA vs Python")

	
14
>>> with open("simple.txt","r") as f:
	f.readline()

	
'JAVA vs Python'
>>> with open("simple.txt","a") as f:
	f.write(  ".python is easy if we know JAVA")

	
31
>>> with open("simple.txt","r") as f:
	f.readline()

	
'JAVA vs Python.python is easy if we know JAVA'
