"""
first - find all lands -- cells == 1 in matrix to list "lands"
second - cycle one by on in lands and check if nearby cells --
    (0, -1), (-1, -1), (-1, 0), (-1, 1) is a land, count all this cells
    also for improve speed -- remove counted cells from "land"
"""


data = [[0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0]]

line_index = -1
lands = []
result = []

for i in data:
    line_index += 1
    column_index = -1
    for ii in i:
        column_index +=1
        if ii == 1:
            lands.append([line_index, column_index])
            
while lands != []:
    z = 1
    one_island = []
    i, j = lands[0][0], lands[0][1]
    
    one_island.append([i, j]) 
    """
    take first land index in land, its garanteed = 1, below for-cycle compare 
    all to this [i, j] cell. hem its done - while cycle take next avalible land-cell
    """
    lands.remove([i, j]) #remove it immediatly
    
    locked_lands = lands[:] #lock(copy) list just in case not to lose cells
    for [a, b] in locked_lands:
        for di, dj in (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1):
            o = a + di
            k = b + dj
            if [o, k] in one_island:
                """
                if nearby cell[o, k] already in one_island, then cell[a, b] connected
                to current land-cell [i, j]
                it's a safe check because cycle goes from left to right and up-down
                you cant miss any cells
                """
                one_island.append([a, b]) 
                if [a, b] in lands: #this check for not-to-remove-it-twice
                    lands.remove([a, b])
                    z += 1
    result.append(z)
print(result)
