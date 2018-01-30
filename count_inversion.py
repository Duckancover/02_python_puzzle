sequence_l = [5, 3, 2, 1, 0]
st = sorted(sequence_l)
ind = -1
r = 0
for i in st:
#    print("==number",i)
    ind += 1
    temp = sequence_l.index(i)
#    print("=======", temp, "ind",ind)
    while temp != ind:
        sequence_l[temp-1], sequence_l[temp] = sequence_l[temp], sequence_l[temp-1]
        r += 1
#        print(r, raw_l)
        temp = sequence_l.index(i)
        
print(r)


