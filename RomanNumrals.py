data = 50
r =""
w = ["I", "V", "X", "L", "C", "D", "M"]
a = [ 1,   5,   10,  50, 100, 500, 1000]
q = [int(i) for i in str(data)]
g = 2*(len(q)-1)
for i in q:
    print (g)
    print (i)
    if i == 5:
        r +=w[g+1]
        
    elif i < 5:
        if i <= 3: 
            r +=w[g]*i
            
        else:
            r += w[g]+w[g+1]
    else:
        if i == 9: 
            r += w[g]+w[g+2]
        else:
            r += w[g+1]+w[g]*(i-5)
    g = g - 2        
    
print (r)
