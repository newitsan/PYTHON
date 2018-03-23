#http://regexlib.com/CheatSheet.aspx

import re
def match1(text):
    pattern=re.compiler("^[a-z]+_[a-z]+$")
    if re.search(pattern,text):
        return "found a match"
    else:
        return "not found a match"
    print(match1("aab_cbbbc"))
    print(match1("aab_Abbbc"))
    print(match1("Aaab_abbbc"))
