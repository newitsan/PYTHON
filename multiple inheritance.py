# multiple inheritance

class student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def displaystu(self):
        print("{}    {}   {}".format(self.name,self.age,self.rollno))
class employee:
    def __init__(self,name,age,rollno,salary,designation):
        student. __init__(self,name,age,rollno)
        self.salary=salary
        self.designation=designation
    def displayemp(self):
        print("{}   {}".format(self.salary,self.designation))
class manager(student,employee):
    def __init__(self,name,age,rollno,salary,designation,admin):
        employee. __init__(self,name,age,rollno,salary,designation)
        self.admin=admin
    def displaymanager(self):
        print("{}".format(self.admin))

obj=manager("santhosh",21,1,120000,'engineer',"yes")
obj.displaystu()
obj.displayemp()
obj.displaymanager()

    
        
