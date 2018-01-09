data = [[0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]]
a = -1
s = []
count = 0
res = []
for i in data:
    a += 1
    b = -1
    for ii in i:
        b +=1
        if ii == 1:
            s.append([a,b])
for [a, b] in s:
    print([a, b])
    for di, dj in (1, 0), (0, 1), (1, 1), (1, -1):
        i, j = a, b
        if [i, j] in s:
            print("ok")
            i += di
            j += dj
            print("dffdf", [i,j])
            count += 1


print(count)
print(len(res))
        
        
        
"""
        
        return res
    for [a, b] in s:
        if [a+1, b] in s:
            count +=1
            s.remove
        if [a+1, b+1] in s:
            count +=1
        if [a, b+1] in s:
            count +=1
"""