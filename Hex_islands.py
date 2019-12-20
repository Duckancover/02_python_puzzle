data = ["B2","B3","C2","C4","D1","D4","E2","E4","F2","F3"]
letter_dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12}
#print(len(data))

arr = [[letter_dict.get(j[0]), int(j[1])] for j in data]
print(arr)

'''
["B2","B3","C2","C4","D1","D4","E2","E4","F2","F3"]:14
["B2","B3","C2","C4","D1","D4","E2","E4","F2"]:9

result
ok_pool
to_check
dont_check
'''
def make_near(data):
    near_cells = []
    near_cells.append([data[0], data[1]-1])
    near_cells.append([data[0], data[1]+1])    
    near_cells.append([data[0]+1, data[1]])
    near_cells.append([data[0]-1, data[1]])    
    if data[0] % 2 == 0:
        near_cells.append([data[0]-1, data[1]+1])
        near_cells.append([data[0]+1, data[1]+1])
    else:
        near_cells.append([data[0]-1, data[1]-1])
        near_cells.append([data[0]+1, data[1]-1])                
    return near_cells
    
def calc_land(ok_pool):
    whole_island = 0
    for i in range(1,13):
        all_land = []
        number_of_land = 0
        for coast in ok_pool:
            if coast[0] == i:
                all_land.append(coast[1])
        if all_land !=[]:
            number_of_land = max(all_land)- min(all_land) + 1
            whole_island += number_of_land
            print(number_of_land)
    return whole_island
    
def check_near(check_cell, allpool, ok_pool=[], to_check=[], dont_check=[], islands=[]):
    #print('check_cell', check_cell)

    near_cells = make_near(check_cell)
    dont_check.append(check_cell)
    add_to_check = [x for x in near_cells if x in allpool and x not in dont_check]
    #to_check_temp2 = [x for x in to_check_temp1 if x not in dont_check]
    #to_check3 = to_check.copy() 
    to_check.extend(add_to_check)
    if ok_pool == []:
        ok_pool.append(check_cell)
    add_to_ok_pool = [x for x in to_check if x not in ok_pool]
    ok_pool.extend(add_to_ok_pool)
    #print(near_cells)
    #print(to_check_temp1, "to_check_temp1")
    #print(to_check3, 'to_check3')
    #print(dont_check, 'dont_check')    
    if to_check != []:
        next_cell = to_check.pop()
        return check_near(next_cell, allpool, ok_pool, to_check, dont_check, islands)
    else:
        print('done---', ok_pool)
        islands.append(calc_land(ok_pool))
        remain_pool = [x for x in allpool if x not in ok_pool]
        if remain_pool == []:
            #calc_land(ok_pool)
            return islands
        ok_pool = []
        to_check=[] 
        dont_check=[]
        return check_near(remain_pool[0], remain_pool, ok_pool, to_check, dont_check, islands)
        
start = arr[0]
print(sorted(check_near(start, arr)))    
    