matrix = (
    (7,0,0,7),
    (7,0,0,7),
    (7,7,0,7),
    (0,0,0,7))

first = (0,1)
second = (3,2)

pattern = [(-1, 0), (0, 1), (1, 0), (0, -1)]
num = matrix[first[0]][first[1]]
print("NUM", num)

all_cell = []
b = []
x = -1

for row in matrix:
    x += 1
    y = -1
    for col in row:
        y += 1
        if col == num:
            all_cell.append((x, y))
print(all_cell)



def check(ilist, all_cell):
    b = []
    for (i, j) in ilist:
        t = 0
        for [di, dj] in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ii = i + di
            jj = j + dj
            if (ii, jj) in all_cell:
                for [ddi, ddj] in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    iii = ii + ddi
                    jjj = jj + ddj
                    if (iii, jjj) in all_cell and (ii, jj) not in b:
                        b.append((ii, jj))
    return print(b)

check([(0,1)], all_cell)

