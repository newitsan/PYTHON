import pickle

apple=[1,2,3,4]
filee=open("apple.pkl","wb")
pickle.dump(apple,filee)
del(apple)
filee=open("apple.pkl","rb")
print(pickle.load(filee))
