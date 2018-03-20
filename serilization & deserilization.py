import pickle
class student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def display(self):
        print(self.name,self.age,self.rollno)

obj=student("java",21,32)

data=open("serilization.pkl","wb")
pickle.dump(obj,data)
data.close()

data=open("serilization.pkl","rb")
pickle.load(data)
print(obj.display())
data.close()

    
