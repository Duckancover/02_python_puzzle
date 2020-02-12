import itertools
'''
grid = [
       [2, 5, 4, 1, 8],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 1]]

maxs = 6
lengh = len(grid)
'''
def upper(grid, path):
    start = (0,0)
    
    def neighbors(grid, start, maxsteps, path):
        res = []
        indexes = itertools.product((1,0,-1), repeat=2)
        for (k, b) in indexes:
            next_cell = x, y = start[0] + k, start[1] + b
            if (0 <= x < len(grid) and 0 <= y < len(grid) and \
            len(grid) - min(next_cell) <= maxsteps - len(path) and next_cell not in path):
                res.append(next_cell)
        return res

    def find_path(maxsteps, fp=[], pw=None):
        tmp = []
        print('_____________')
        end = (len(grid)-1, len(grid)-1)
        print(end)
        if pw is None:
            pw = []
            pw.append([start])
        print(pw)
        for i in pw:
            print(i, 'i')
            if i[-1] == end:
                fp.append(i)
                print(i)
            next_steps = neighbors(grid,i[-1], maxsteps, i)
            print(next_steps, 'next_steps')
            for j in next_steps:
                print('j',j)
                ss = i.copy()
                ss.append(j)            
                if j == end:
                    fp.append(ss)
                else:
                    tmp.append(ss)
        if tmp == []:
            print(fp, 'here')
            return fp
        print(tmp,'tmp')
        return find_path(maxsteps, fp, tmp)

    
        
        
        
        
    res = find_path(path)
    rres = []
    for ii in res:
        print(ii)
        g = sum([grid[a][b] for (a, b) in ii])
        rres.append(g)
    
    print(max(rres))
    return rres

upper([[1, 6],
                  [5, 1]], 2)    