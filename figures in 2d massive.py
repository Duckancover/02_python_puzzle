data = '''
001203
023001
100220
'''

def figure(start, connected=[], to_check=[]):
    #print('_____')
    if connected == []:
        connected.append(start)
    k = start[0]
    b = start[1]
    neighbors = [(k, b+1), (k, b-1), (k+1, b), (k-1, b)]
    for x, y in neighbors:
        if all(index >= 0 for index in (x,y)):
            #print(x, y)
            try:
                if lines[x][y] != '0' and (x, y) not in connected:
                    connected.append((x, y))
                    to_check.append((x, y))
            except IndexError:
                pass
    if to_check != []:
        #print(to_check)
        return figure(to_check.pop(), connected, to_check)
    print(connected)    
    return connected

lines = [i for i in data.split('\n') if len(i)>0]
result = []
allnumbers = []
for idx, line in enumerate(lines):
    for idy, i in enumerate(line):
        if i != '0':
            point = (idx, idy)

            if point not in allnumbers:
                fig = figure(point, [], [])
                result.append([int(lines[k][b]) for (k, b) in fig])
                allnumbers.extend(fig)
                
summ = list(map(sum, result))
print(sorted(summ, reverse=True))