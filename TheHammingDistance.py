# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:56:45 2017

@author: Oleg.Shcherbinin
"""

def checkio(n, m):    
    return bin (n ^ m).count("1")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    print("ok")