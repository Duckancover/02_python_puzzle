# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:04:44 2017

@author: Oleg.Shcherbinin
"""

a = ["b3", "a4", "c4", "e1", "d2"]
y = 0
pawnid = set()
for i in a:
    row = int(i[1])-1
    col = ord(i[0])-97
    pawnid.add((row, col))
#print (pawnid)
for i in pawnid:
    b = (i[0]-1,i[1]-1)
    c = (i[0]-1,i[1]+1)
    for t in pawnid:
        if t == c or t == b:
            y += 1
print (y)