#To check that a string contains a particular character
import re
def display(string):
    x=re.compile(r"[^a-zA-Z0-9!@#$%^&*)(}{]")
    string=x.search(string)
    return not bool(string)

print(display("abcdABCD012345"))
print(display("!@#$%^&*)(}{"))
