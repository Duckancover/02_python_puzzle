m = [-50, 50, 1]
z = 0
def rlen(y):
    if len(y) == 0:
        return print("cvbcbcvb",z)
        
    else:
        return popsum(y)
        
def popsum(x):
    global z
    z = z + x.pop()
    print (z)
    return rlen(x)
#    return z 

popsum([2,2,2,2,2,2])
