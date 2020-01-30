# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:57:05 2020

@author: Shcherbinin


"""

def make_number(a):
    dictt ={
    '0':"",
    '00':"",
    '1':"one",
    '2':"two",
    '3':"three",
    '4':"four",
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '10':'ten',
    '11':'eleven',
    '12':'twelve',
    '13':'thirteen',
    '14':'fourteen',
    '15':'fifteen',
    '16':'sixteen',
    '17':'seventeen',
    '18':'eighteen',
    '19':'nineteen',
    '20':'twenty',
    '30':'thirty',
    '40':'forty',
    '50':'fifty',
    '60':'sixty',
    '70':'seventy',
    '80':'eighty',
    '90':'ninenty',
    'hun':'hundred',
    '1000':'thousand'}
    
    #a = 103
    c = str(a)
    d = [i for i in c]
    hun = '0'
    tens = '0'
    res = []
    '''
    if len(d) == 4:
        print('1000')
    elif len(d) == 3:
        if d[1] == '1' or d[1] == '2':
            print(dictt[''.join(d[1:3])])
            print(dictt[d[0]],dictt['hun'])
        else:
            sin = d[-1]
            tens = ''.join([d[1], '0'])
            hun = d[0]
            print(' '.join([dictt[hun], dictt['hun'], dictt[tens], dictt[sin]]))
    '''        
    
    if len(d) == 4:
        return print('1000')
    if len(d) >= 3:
        hun = d[-3]
        res.extend([dictt[hun], dictt['hun']])
    if len(d) >= 2:
        if d[-2] == '1':
            tens = ''.join([d[-2],d[-1]])
            res.append(dictt[tens])
        else:
            tens = ''.join([d[-2], '0'])
            sin = d[-1]
            res.extend([dictt[tens], dictt[sin]])
    if len(d) == 1:
        return dictt[d[-1]]
    
    #print(' '.join([dictt[hun], dictt['hun'], dictt[tens], dictt[sin]]))  
    
    ress = [i for i in res if len(i)>0]
    return ' '.join(ress)

H = 999

long = [make_number(i) for i in range(1,H+1)]
long.sort()
end = long.index(make_number(H))+1
print('position', end, '|', 'ID', end-1)