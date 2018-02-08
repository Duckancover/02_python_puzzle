
number = 371

r = 0
l = [ int( i*(i+1) / 2 ) for i in range(46)]
#l = [int(i) for i in l]
#print(l)

def Sum(l, number, start=0):
    r = 0
    res = []
    for i in range(start, 50):
        if l[i] > number:
             return print("no")           
        r += l[i]
        res.append(l[i])
        if r == number:
            return print("ok", res)
        if r > number:
            start += 1
            return Sum(l, number, start=start) 

Sum(l, number)
           
