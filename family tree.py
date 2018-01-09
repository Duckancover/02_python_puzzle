# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:58:00 2018

@author: Oleg.Shcherbinin
"""

def is_family(tree):
    sons = []
    origin_name = ""
    dads = []
    count = 0
    for i in tree:

        if i[0] == i[1]:
            return False
        if i[0] not in dads:
            dads.append(i[0])
        if i[1] not in sons:
            sons.append(i[1])
        else:
            return False 
    for i in dads:
        if i not in sons:
            origin_name = i
    for [a, b] in tree:
        if [b, a] in tree:
            return False
            
#    if origin_name == "":
#        return False 
    
    for i in dads:
        if i in sons:
            count += 1
    if len(dads) - count == 1:
        return True
    else:
        return False 


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")