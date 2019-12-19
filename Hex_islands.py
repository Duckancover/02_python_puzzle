data = ['A1','A2','A3','A4','B1','B4','C2','C5','D2', 'D3','D4','D5','H6','H7','H8','I6','I9','J5','J9','K6','K9','L6','L7','L8']
letter_dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12}
print(len(data))

arr = [[letter_dict.get(j[0]), int(j[1])] for j in data]
print(arr)

'''
result
ok_pool
to_check
dont_check
'''
def make_near(data):
    near_cells = []
    near_cells.append([data[0]-1, data[1]])
    near_cells.append([data[0]-1, data[1]+1])
    near_cells.append([data[0]+1, data[1]+1])
    near_cells.append([data[0]+1, data[1]])
    near_cells.append([data[0], data[1]-1])
    near_cells.append([data[0], data[1]+1])
    return near_cells
def check_near(check_cell, allpool, ok_pool=[], to_check=[], dont_check=[], islands=[]):
    print('check_cell', check_cell)

    near_cells = make_near(check_cell)
    dont_check.append(check_cell)
    to_check_temp1 = [x for x in near_cells if x in allpool]
    to_check_temp2 = [x for x in to_check_temp1 if x not in dont_check]
    to_check3 = to_check.copy()
 
    to_check3.extend(to_check_temp2)
    if ok_pool == []:
        ok_pool.append(check_cell)
    add_to_ok_pool = [x for x in to_check3 if x not in ok_pool]
    ok_pool.extend(add_to_ok_pool)
    #print(near_cells)
    #print(to_check_temp1, "to_check_temp1")
    print(to_check3, 'to_check3')
    print(dont_check, 'dont_check')
    
    if to_check3 != []:
        next_cell = to_check3.pop()
        return check_near(next_cell, allpool, ok_pool, to_check3, dont_check, islands)
    else:
        print('done---', ok_pool)
        islands.append(len(ok_pool))
        remain_pool = [x for x in allpool if x not in ok_pool]
        if remain_pool == []:
            return print('all done', islands)
        ok_pool = []
        to_check=[] 
        dont_check=[]
        return check_near(remain_pool[0], remain_pool, ok_pool, to_check, dont_check, islands)
        
start = arr[0]
check_near(start, arr)    
    