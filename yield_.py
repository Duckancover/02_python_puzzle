import itertools

grid = [
       [1,2,3],
       [9,4,5],
       [6,8,0]]
maxs = 4
lengh = len(grid)

def neighbors(grid, start, maxsteps, path):
    res = set()
    indexes = itertools.product((1,0,-1), repeat=2)
    for (k, b) in indexes:
        next_cell = x, y = start[0] + k, start[1] + b
        if (0 <= x < len(grid) and 0 <= y < len(grid) and \
        len(grid) - min(next_cell) <= maxsteps - len(path) and next_cell not in path):
            res.add(next_cell)
    return res

def find_path(grid, start, maxsteps, path=None):
    end = len(grid)-1, len(grid)-1
    if path is None:
        path = set()
        path.add(start)
    if start == end:
        yield path
    next_steps = set(neighbors(grid,start, maxsteps, path))
    for step in next_steps:
        new_path = path.union(step)
        yield from find_path(grid, step, maxsteps, new_path)
        
res = find_path(grid, (0,0), maxs)
#dd = neighbors(grid, (1,1), maxs, {(0,0), (1,1)})
print(dd)
next(res)
next(res)
next(res)
next(res)     
    