number = 255000000000
base = 1000
decimals=0
suffix=''
powers=['', 'd', 'M']
ff = ""

num = abs(number)
n_based = []
power = 0
dig = len(str(base))-1
print("dig=", dig)
print(len(powers))

while num >= base:
    x = divmod(num, base)
    if x[1] == 0:
        n_based.append("0"*dig)
    else:
        n_based.append(str(x[1]))
    num = x[0]
    power += 1
print("poer",power)
if power >= len(powers):
    ind = powers[-1]
    ff = str(power - len(powers) -1)
else:
    ind = powers[power]
    
    
n_based.append(str(num)) 
n_based.reverse()
n_str = "".join(n_based)



if decimals == 0:
    core_n = str(round(int(n_str)//(10 ** (dig * power)), decimals))
    print("xxxxxxxxxxxxx",core_n)

else:
    nice_number = str(round(int(n_str)/(10 ** (dig * power)), decimals))
    core_n = nice_number.ljust(nice_number.find(".")+decimals+1, "0")

z = [core_n, ff, ind,suffix]
print(core_n)


if number < 0:
    print("-"+"".join(z))
else:
    print("".join(z))
    

