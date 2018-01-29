# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:17:37 2018

@author: Oleg.Shcherbinin
"""

import re
phrase = "hieeelalaooo"
a = "aeiouy"

result = re.findall(r'([^aeiouy ])\w', phrase)
#print(result)
z = re.sub(r'[^aeiouy ]\w', "{}", phrase)
c = z.format(*result)

for i in a:
    ii = "["+i+"]{3}"
    #print(ii, type(ii))
    zz = re.sub(ii, i, c)
    c = zz
    
print(c)
    
