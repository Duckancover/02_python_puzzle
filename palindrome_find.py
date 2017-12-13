a = "abbaoerty7ytre"
res = []

start = -1
for ii in range(len(a)-1):
    start +=1
    i = -1
    for item in a:
        i += 1
        x = a[i::-1]
        lenp = (i+1) * 2 + 1
        #print("xxxxxxxx",x)
        #print(lenp,"lenght")
        b = a.find(x,lenp // 2,lenp)
        #print(b,"found indx")
        if b == i + 1:
            z = a[0:b]+a[b:lenp-1]   #no middle letter
        elif b == i + 2:
            z = a[0:b]+a[b:lenp]   #middle letter
    res.append(z)
    a = a[1:]
    print("------------------",z)
    print("******************************",a)

print(bb)

res2 = []
for i in res:
    res2.append(len(i))

