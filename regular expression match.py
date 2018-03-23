#http://regexlib.com/CheatSheet.aspx
import re

def match(text):
    pattern=re.compile("san*?")
    if re.search(pattern,text):
        return "found a match"
    else:
        return "not match"

print(match("san"))
print(match("nas"))
print(match("sat"))
