check = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        }
roman_string = 'LXXVI' #76

res = []
r = 0

for i in roman_string:
    res.append(check.get(i))
    
print(res)
    
for i in range(len(res)-1):
    if res[i] >= res[i+1]:
        r += res[i]
    else:
        r -= res[i]
        
print(r+res[-1])
    
    
    
    