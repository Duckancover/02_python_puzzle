a = 7
a9 = bin(a)[2:]
b = 2
b9 = bin(b)[2:]

zz = []
yy = []
ww = []
res = 0

for i in a9:
    z = [str(int(i) & int(j)) for j in b9]
    y = [str(int(i) | int(j)) for j in b9]
    w = [str(int(i) ^ int(j)) for j in b9]
    #p = "".join(z)
    yy.append("".join(y))
    zz.append("".join(z))
    ww.append("".join(w))

All = [yy, zz, ww]
    
for i in All:
    r = 0
    for j in i:
        r += int("0b"+j, 2)
    res +=r
    
print(res)