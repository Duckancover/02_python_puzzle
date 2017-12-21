number = 4000000001
base = 1024
decimals=1
suffix=''
powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
ff = ""

num = abs(number)
n_based = []
power = 0
dig = len(str(base))-1
if dig == 0:
    dig = 1
print("dig=", dig)
#print(len(powers))

while num >= base:
    x = divmod(num, base)

    if len(str(x[1])) < dig:
        n_based.append("0"*dig)
    else:
        n_based.append(str(x[1]))
    num = x[0]
    power += 1
print(power)
print(n_based)

    
if power >= len(powers):
    power2 = powers[-1]
    power = len(powers) - 1
else:
    power2 = powers[power]
   
    
n_based.append(str(num)) 
n_based.reverse()
n_str = "".join(n_based)

print("n_str==", n_str)

if decimals == 0:
    core_n = str(round(int(n_str)//(10 ** (dig * power)), decimals))
    if base < 30:
        core_n = str(int(core_n, base))
    

else:
    nice_number = str(round(int(n_str)/(10 ** (dig * power)), decimals))
    core_n = nice_number.ljust(nice_number.find(".")+decimals+1, "0")

z = [core_n, power2, suffix]
print(core_n)


if number < 0:
    print("-"+"".join(z))
else:
    print("".join(z))
    

