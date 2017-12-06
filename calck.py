m = [-50, 50, 1]

def popsum(z, x):
    z += x.pop()
    #print (z)
    return rlen(z, x)


def rlen(z, y):
    if len(y) == 0:
        return print(z)
                
    else:
        return popsum(z, y)

def push(x):
    z = 0
    return popsum(z, x)

push([1,2,2,2,2,2]) # 11
push([1,2,2,2,2]) #9

