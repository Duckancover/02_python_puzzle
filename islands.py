data = [[0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]]
#          [2, 3, 3, 4]

line_index = -1
lands = []
one_island = []
count_land_island = 0
result = []
for i in data:
    line_index += 1
    column_index = -1
    for ii in i:
        column_index +=1
        if ii == 1:
            lands.append([line_index, column_index])
for [line_index, column_index] in lands:
    i, j = line_index, column_index
    t = 0
    print("============UP layer", line_index, column_index)
    if [i, j] not in one_island:
        count_land_island += 1
    for di, dj in (0, 1), (1, 1), (1, 0), (1, -1):
        i = line_index + di
        j = column_index + dj
        print("current i j ", [i, j])
        if [i, j] in lands:
            t += 1
            if [i, j] not in one_island:
                one_island.append([i, j])
                count_land_island +=1
            print("                match",[i, j])
            print("                ",one_island)
            print(count_land_island, t)

        
    if t == 0:
        result.append(count_land_island)
        count_land_island = 0

print(result)
        
"""
        return res
    for [a, b] in s:
        if [a+1, b] in s:
            count +=1
            s.remove
        if [a+1, b+1] in s:
            count +=1
        if [a, b+1] in s:
            count +=1
"""