data = 90

I = 1 #0
V = 5 #1
X = 10 #2
L = 50 #3
C = 100 #4
D = 500
M = 1000
r = []
w = ["I", "V", "X", "L", "C"]
a = [1, 5, 10, 50, 100]
count = -1
for i in a: 
    if data // i > 0:
        count +=1
        print("fff",count)
#if count % 2 == 0:
#    count +=1
print ("count",count)


q = [9, 0]
for i in q:
    print ("____________________________")
    if i % 5 >= 4:
        print ("hre", 1)
        r.append((w[count-1], w[count+1]))
        print ("iftrue",r)
    else:
        r.append(w[count]*(i % 5))
        print ("elsetrue",r)
    count -=1

print (r)



"""
if y >= 4:
    print ("X",(10-data)*"I")
else:
    print ("V", y*"I")  
print (y, x) 
"""