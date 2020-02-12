
num = set([10, 13, 14, 15])
#data.add(*[2,6,7,10])

FIG = dict(L = [(1, 0),
                (1, 0),
                (1, 1)],
                
           T = [(1, 1, 1),              
                (0, 1, 0)],
                
           J = [(0, 1),
                (0, 1),
                (1, 1)],
                
           S = [(0, 1, 1),              
                (1, 1, 0)],
                
           Z = [(1, 1, 0),              
                (0, 1, 1)],
                
           I = [(1,1,1,1)],
            
           O = [(1, 1),
                (1, 1)])

def rotate(grid):
    r = list(zip(*reversed(grid)))
    #print(*r, 'rot', sep='\n')
    return r

#grid= [[0,0,0,0] for i in (1,2,3,4)]
'''
tr =[]
for i in data:
    if i % 4 == 0:
        x = i//4 - 1
        y = 3
        print(i//4 - 1, 3)
    else:
        x = i//4
        y = i % 4 - 1        
        print(i//4, i % 4 - 1)
    grid[x][y] = 1
    tr.append((x, y))
print(grid)    

def rotate(grid):
    r = list(zip(*reversed(grid)))
    #print(*r, 'rot', sep='\n')
    return r


def chunk(grid):
    res = [i for i in grid if sum(i) !=0]
    temp = rotate(res)
    res = [i for i in temp if sum(i) !=0]
    #print(*res,  're', sep='\n')
    return res

let = chunk(grid)

print(*let, 'let', sep='\n')
'''

fig_idxs =[]
for i in num:
    if i % 4 == 0:
        x = i//4 - 1
        y = 3
        print(i//4 - 1, 3)
    else:
        x = i//4
        y = i % 4 - 1        
        print(i//4, i % 4 - 1)
    fig_idxs.append((x, y))

d_line, d_col = list(map(min, zip(*fig_idxs)))
grid = [[0] * (d_line+1) for i in range(d_col+1)]

#fig_idx = [(x -d_line, y - d_col) for (x,y) in tr]

print(*grid, sep='\n')


for x, y in fig_idxs:
    newX, newY = x -d_line, y - d_col
    grid[newX][newY] = 1
    
let = rotate(grid)

for i in (90, 180, 270, 360):
    for key, sh in FIG.items():
        if sh == let:
            print(key,'<--------------------------------------')
    let = rotate(let)
    print(*let, 'rlet', sep='\n')
    
    
============
fig_idxs =[]
for i in num:
    if i % 4 == 0:
        x = i//4 - 1
        y = 3

    else:
        x = i//4
        y = i % 4 - 1        

    fig_idxs.append((x, y))

d_line, d_col = list(map(min, zip(*fig_idxs)))

#print('test', list(zip(*fig_idxs)))
ness = []

for i, j in fig_idxs:
    a, b = i - d_line, j - d_col
    ness.append((a,b))
    

    
col = list(zip(*ness))
    

grid = [[0] * (max(col[1])+1) for i in range(min(col[0])+1)]
'''
for (x,y) in ness:
    grid[x][y] = 1
'''   
  
print(*grid, sep='\n')
============
    
  