# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 10:49:28 2017

@author: Oleg.Shcherbinin
"""
a = ["X.O",
     ".XO",
     "XOO"]

for i in a:
    if i[0] == i[1] == i[2]:
        print (i[0], "1is win")
        break          
for i in range(3):
    x = [row[i] for row in a]
    if x[0] == x[1] == x[2]:
        print (x[0], "2is win")  
        break
    elif a[0][2] == a[1][1] == a[2][0]:
        print (a[1][1], "is win")
        break
    elif a[0][0] == a[1][1] == a[2][2]:
        print (a[1][1], "is win")
        break        
else:
    print('no winner')
        