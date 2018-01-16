state = [1, 0, 0, 0, 1, 1, 0, 1]
#   5   [0, 1, 1, 0, 1, 1, 0, 0]
pipe_numbers = [5, 4, 5]

pipe_numbers_clear = list(set(pipe_numbers))
a = len(state)
res = []

position_loader = [0 for i in range(a)]
temp = [0 for i in range(a)]
for i in pipe_numbers_clear:
    position_loader[i] = 1
for r in range(a):
    sss = 1
    for i in range(a):
        temp[i] = state[i-r]
    print(temp)
    for k in range(a):
        if position_loader[k] == 1:
            if temp[k] == 1:
                sss = 0
            else:
                sss = 1
                break
    if sss == 0:
        print(r,"ok")
        res.append(r)

print(res)

"""
for i in range(a):
    if z[i] == 1:
        if z[i] == state[i]:
            sss = 0
        else:
            sss = 1
            print("no")
            break
if sss != 1:
    print("ok")
"""