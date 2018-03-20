import re

s1="sday,mday,tday,wday,tday,fday,sday"
day=re.findall("[a-z]day",s1)
for i in day:
    print(i)
