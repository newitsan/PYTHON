import re

str="python is a good programming language and i am studying python"
#str1= re.finditer("python",str)  # this is valid method as well.
#for i in str1:
  #  print(i)

for i in re.finditer("python",str):
    x=i.span()
    print(x)
