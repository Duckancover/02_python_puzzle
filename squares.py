# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:36:34 2017

@author: Oleg.Shcherbinin
"""

a = [[3, 4], [6, 2], [2, 3],[10, 11]]
len1 = []
len2 = []
len3 = []
a1 = [sorted(i) for i in a]
print(a1)


for i in range(1,13):
    if [i, i+1] in a1:
        len1.append([i, i+1])
        if [i+1, i+2] in a1:
            len2.append(([i, i+1],[i+1, i+2]))
            if [i+2, i+3] in a1:
                len3.append(([i, i+1],[i+1, i+2],[i+2, i+3]))



    

print("len1==",len1)
print(len2)