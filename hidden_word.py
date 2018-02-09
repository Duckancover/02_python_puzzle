import re
from itertools import zip_longest
word = "haoo"
print(word[0])
rhyme = "Hi all!\nAnd all goodbye!\nOf course goodbye.\nor not"

offset = len(word)
ry2 = re.split('\n', re.sub(" ", "", rhyme.lower()))

f = list(zip_longest(*ry2, fillvalue='_'))
ff = ["".join(i) for i in f]
    
for i in ry2: #horiontal
    u = i.find(word)
    if u != -1:
        print(ry2.index(i), u)
        res = [ry2.index(i)+1, u+1, ry2.index(i)+1, u+offset]
          
for i in ff: #vertical
    u = i.find(word)
    if u != -1:
        print(ff.index(i), u)
        res = [ff.index(i)+1, u+1, ff.index(i)+1, u+offset]
        
print(res)