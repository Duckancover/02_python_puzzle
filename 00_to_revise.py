# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:44:44 2017

@author: Oleg.Shcherbinin
"""

def checkio(a):
    r = -1
    c = -1
    hh = 0
    for i in a:
        r += 1
        for ii in i:
            c += 1
            if foo(a, r, c) is True:
                hh += 1
                break
    if hh == 1:
        return True
    else:
        return False


def foo(a, r, c, res=0, z=0):
    try:
        if a[r][c] == a[r][c+1]:  #to right
                res +=1
                z = 0
                return foo(a, r, c+1, res, z)
        if a[r][c] == a[r+1][c+1]:  #to diag down
            res +=1
            return foo(a, r+1, c+1, res)
        if a[r][c] == a[r+1][c]:  #to down
            res +=1
            return foo(a, r+1, c, res)
        if a[r][c] == a[r-1][c+1]:  #to diag up
            res +=1
            return foo(a, r-1, c+1, res)
        
    except IndexError:
        pass
    if res >= 3:
        return True
    else:
        return False
      

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
