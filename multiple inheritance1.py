class student:
    def __init__(self,name,age,rollno):
	    self.name=name
	    self.age=age
	    self.rollno=rollno
    def displaystu(self):
	    print("Name of the student= %s"  % self.name)
	    print("Age of student=  %s"  % self.age)
	    print("Rollno of student= %s" % self.rollno)
class employee:
    def __init__(self,name,age,rollno,salary,designation):
                    student. __init__(self,name,age,rollno)
                    self.salary=salary
                    self.designation=designation
    def displayemp(self):
	    print("salary of employee= %s" % self.salary)
	    print("designation of employee= %s" % self.designation)
class manager(student,employee):
    def __init__(self,name,age,rollno,salary,designation,admin):
	    employee. __init__(self,name,age,rollno,salary,designation)
	    self.admin=admin
    def displaymanager(self):
	    print("is access given to manager?   %s" % self.admin)
obj=manager("santhosh",21,32,100000,"manager","yes")
obj.displaystu()
obj.displayemp()
obj.displaymanager()
