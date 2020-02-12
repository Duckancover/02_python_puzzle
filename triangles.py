# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:19:22 2020

@author: Shcherbinin
"""
import math
import itertools
data = [[7,2],[3,2],[1,5],[3,9],[7,9],[9,6]] #40
d = itertools.combinations([1,2,3,4,5], 2)
print(list(d))

def tri(data):
    A, B, VERT = data
    if A[0] - B[0] == 0:
        normal = VERT[0] - A[0]
    elif A[1] - B[1] == 0:
        normal = VERT[1] - A[1]
    else:
        k = (B[1]-A[1]) / (B[0]-A[0])
        b = A[1] - k * A[0]
        normal = (k * VERT[0] - VERT[1] + b) / math.sqrt(k ** 2 + 1)
    base = math.hypot((A[0]-B[0]),(A[1]-B[1]))
    pl = abs(normal) * abs(base) / 2
    print(pl)
    return pl

res = 0
for i in range(1, len(data)-1):
    a, b = i, i+1
    idx = (data[0], data[a], data[b])
    print(idx)
    c = tri(idx)
    res +=c
    
print(res,'res')
    
