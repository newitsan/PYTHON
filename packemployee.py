from .packstudent import *

class employee(student):
    def __init__(self,name,age,rollno):
        student. __init__(self,name,age)
        self.rollno=rollno
    def displayemployee(self):
        print("employee designation is=%s"  % self.rollno)
