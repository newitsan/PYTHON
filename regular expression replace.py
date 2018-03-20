#replace a string
import re

s1="java is a good programing language and i am learning java"
replace=re.compile("java")
print(replace.sub("python",s1))

