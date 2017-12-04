# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:44:35 2017

@author: Oleg.Shcherbinin
"""
a = ('Return the highest index in S where substring sub is found,such applehat sub is contained within S[start:end].  Optionalarguments start and end are interpreted as in slice notat')
b = ["how", "are", "you", "no", "hat", "sub", "apple"]
import re
c = [i for i in b if re.search(i, a) != None]
print (c)
