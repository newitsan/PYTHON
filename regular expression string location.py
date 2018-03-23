import re


text="a quick brown fox jumps over the lazy dog"
pattern="dog"
match=re.search(pattern,text)
a=match.start()
b=match.end()
print('found "%s" in "%s" from %d to %d'   %(match.re.pattern,match.string,a,b))
