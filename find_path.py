def can_pass(matrix, first, second):
    
    num = matrix[first[0]][first[1]]
    
    all_cell = []
    x = -1
    
    for row in matrix:
        x += 1
        y = -1
        for col in row:
            y += 1
            if col == num:
                all_cell.append((x, y))
    return f1(all_cell, second, [first])

def f1(all_cell, second, start_l, block_l=[]):
    target_l = []
    for (i, j) in start_l:
        for (di, dj) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ii = i + di
            jj = j + dj
            if (ii, jj) in all_cell:
                for [ddi, ddj] in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    iii = ii + ddi
                    jjj = jj + ddj
                    if (iii, jjj) == second:
                        return True
                    if (iii, jjj) in all_cell and (ii, jj) not in block_l:
                        target_l.append((ii, jj))
                        block_l.append((ii, jj))
    block_l += start_l
    if target_l == []:
        return False
    return f2(all_cell, second, target_l, block_l)
    
def f2(all_cell, second, prev_targ, block):
    return f1(all_cell, second, prev_targ, block_l=block)





if __name__ == '__main__':
    assert can_pass(((5,6),
                     (6,6),
                     (6,5),
                     (6,6),
                     (7,6),
                     (6,6),
                     (6,7),
                     (6,6),
                     (8,6),
                     (6,6)), 
                    (9,1), (0,1)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
    print("ok!")
