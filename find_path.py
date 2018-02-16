def can_pass(matrix, first, second):
    
    
    num = matrix[first[0]][first[1]]
    all_cell = []
    for row_id, val in enumerate(matrix):
        for col_id, val2 in enumerate(val):
            if val2 == num:
                all_cell.append((row_id, col_id))
                
    return f1(all_cell, second, [first], [first])

def f1(all_cell, second, start_l, block_l):
    
    
    target_l = []
    for (i, j) in start_l:
        for (di, dj) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            next_cell_i = i + di
            next_cell_j = j + dj
            if (next_cell_i, next_cell_j) in all_cell:
                for [ddi, ddj] in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    coherently_cell_i = next_cell_i + ddi
                    coherently_cell_j = next_cell_j + ddj
                    if (coherently_cell_i, coherently_cell_j) == second:
                        return True
                    if (coherently_cell_i, coherently_cell_j) in all_cell and (next_cell_i, next_cell_j) not in block_l:
                        target_l.append((next_cell_i, next_cell_j))
                        block_l.append((next_cell_i, next_cell_j))
                        
    block_l.extend(start_l) #because start_list already checked and not needed anynore
    
    if target_l == [] :
        return False
    return f1(all_cell, second, target_l, block_l)
    


if __name__ == '__main__':
    assert can_pass(((0, 2, 2),
                      (0, 2, 2),
                      (0, 0, 0),),
                      (0,0), (2,2)) == True, 'First example'
    assert can_pass(((0, 2, 2),
                      (0, 2, 2),
                      (0, 0, 0),),
                      (0,0), (2,2)) == True, 'First example'
    assert can_pass(((0, 2, 2),
                  (0, 2, 2),
                  (0, 0, 0),),
                  (0,0), (2,2)) == True, 'First example'
    


    print(1)
    

