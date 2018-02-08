import re
from itertools import zip_longest
word = "noir"
print(word[0])
rhyme = """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!"""


#ry = re.sub(" ", "", rhyme)
ry2 = re.split('\n', re.sub(" ", "", rhyme))
p = []
for i in ry2:
    p.append([i])
    print(len(i))
    
for i in ry2: #horiontal
    u = i.find(word)
    if u != -1:
        print(ry2.index(i), u)
        res = [ry2.index(i), u, ry2.index(i), u+len(word)-1]
    
#f = zip(ry2[i] for i in range(len(ry2)))
        
f = list(zip_longest(ry2[0], ry2[1], ry2[2], ry2[3], fillvalue='_'))
ff = []
for i in f:
    ff.append("".join(i))
    
for i in ff: #vertical
    u = i.find(word)
    if u != -1:
        print(ff.index(i), u)
        res = [ff.index(i), u, ff.index(i), u+len(word)-1]