import pickle
class student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def display(self):
        print("enter {}".format(self.name))
        print("enter %s" % self.age)
        print("enter %s" % self.rollno)

s=student("migen",3,4)
s.display()

file=open("serilization.pkl","wb")
pickle.dump(s,file)

file=open("serilization.pkl","rb")
print(pickle.load(file))
