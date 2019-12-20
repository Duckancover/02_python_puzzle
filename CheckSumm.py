import re
data = "VQ/WEWF/NY/8U"
all_numbers_letters = re.findall(r'[0-9A-Z]', data)
code = "".join(all_numbers_letters)
print(code)
reversed_code = code[::-1]
summ = 0
for idx, i in enumerate(reversed_code):
    if idx % 2 == 0:
        x = (ord(i) - 48) * 2
        print('>9', idx, x)
        if x > 9:
            x = x // 10 + x % 10
            print('here',idx, i, x)    
    else:
        x = ord(i) - 48
    summ += x
if summ % 10 == 0:
    summ = 0
result = 10 - summ % 10    
print(result,summ)
        