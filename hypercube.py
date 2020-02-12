# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:06:07 2020

@author: Shcherbinin
"""

import itertools

grid =     [['g', 'f', 'H', 'Y', 'v'],
            ['z', 'e', 'a', 'P', 'u'],
            ['s', 'B', 'T', 'e', 'y'],
            ['k', 'u', 'c', 'R', 't'],
            ['l', 'O', 'k', 'p', 'r']]


def hypercube(grid):
    pool = []
    def relatedcells(start_index, wordindex=1):
        print('+++++++')
        sx, sy = start_index
        indexes = [(-1,0),(1,0),(0,-1),(0,1)]
        for k, b in indexes:
            position = x, y = sx+k, sy+b
            print(position, 'position')
            if 0 <= x <= len(grid)-1 and 0 <= y <= len(grid)-1:
                print(grid[x][y])
                if grid[x][y].upper() == word[wordindex]:
                    wordindex += 1
                    if wordindex < 9:
                        return relatedcells(position, wordindex)
                    else:
                        print('good')
                        return 1
        else:
            print('NO good int')
            return 0
           
    
    word = 'HYPERCUBE'
    for i, line in enumerate(grid):
        for j, let in enumerate(line):
            #print(let, 'let')
            if let.upper() == 'H':
                pool.append((i,j))
                #return relatedcells((i, j), 1)
    print(pool)
    for st_point in pool:
        print('-----------------')
        if relatedcells(st_point, 1) == 0:
            print('out no')
            pass
        else:
            print('out good')            
            return True
            
    return False

            
hypercube([['h', 'a', 'r', 'a'], 
           ['y', 'p', 'e', 'a'], 
           ['e', 'b', 'r', 'c'], 
           ['a', 'u', 'c', 'a']])

                
    

            
        