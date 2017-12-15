data = [5, 3]

r = len(data)
c = 0
for item in data:
    c +=1
    print(c, item,"iter------------------------------")
    r1 = 0
    y = 1
    for i in range(len(data)-1):
        if item <= data[i+1]:
            y +=1
            print("y--",y, "i----",i)
        else:
            break
    r1 = y * item
    if r1 > r:
        r = r1
    data = data[1:]
#    print(data)
    
print(r,"result")

