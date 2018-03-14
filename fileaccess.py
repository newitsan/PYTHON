class display:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return("%s %s" %(self.name,self.age))

#import file
#same folder but different filename

    #from greenpython.fileaccess import display
from fileaccess import display
f=[display("santhosh",16),display("priya",30)]
for i in f:
    print(i)

    # output

    santhosh 16
    priya 30

    
