# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:40:20 2017

@author: Oleg.Shcherbinin
"""

def checkio(expression):
    d = {"{":1, "[":2, "(":3}
    e = []
    f = {"}":1, "]":2, ")":3}
    for i in expression:  
        if i in d.keys():
            e.append(d[i])
        if i in f.keys():
            try:
                if f[i] == e[-1]:
                    e.pop(-1)
                else:
                    return False
            except IndexError:
                return False
    if len(e) == 0:
        return True
    else:
        return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    print ("OK")