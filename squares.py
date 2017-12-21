# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:36:34 2017

@author: Oleg.Shcherbinin
"""

a = [[3, 4], [6, 2], [2, 3],[11, 12],[4,8],[8,12],[10,11],[6,10],[6,7],[3,7]]
len1 = []
len2 = []
len3 = []
c = 0
a1 = [sorted(i) for i in a]
print(a1)


for i in range(1,12):
    if [i, i+1] in a1:
        len1.append([i, i+1])
        if [i+1, i+2] in a1:
            len1.append([i, i+1, i+2])
            if [i+2, i+3] in a1:
                len1.append([i, i+1, i+2, i+3])

print("len1==",len1)
print(len(a1[0]))

for r in len1:
    c += 1
    print("iter----------", c)
    for i in range(1, len(r)):
        x = 4*(i-1)
        y = 4*i
        print(r[0]+x, r[0]+y)
        print(r[-1]+x, r[-1]+y) 
        #print(r[0]+4 * (len(r)-1), r[0]+4 * (len(r)-1)+1)
        if [r[0]+x, r[0]+y] not in a1:
            break
        elif [r[-1]+x, r[-1]+y] not in a1:
            break
        elif[r[0]+(4 * (len(r)-1)), ] not in a1:
            break
        else:
            print("good")
       

            
