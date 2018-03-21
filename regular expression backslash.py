#regular expression with back slash
import re

num="123456789"
print(len(re.findall(r"\d{5}",num)))


