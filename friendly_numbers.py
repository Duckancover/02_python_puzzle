number = 4294967297
base = 2
decimals=0
suffix=''
powers=["p0","p1","p2","p3","p4","p5","p6","p7","p8","p9","p10","p11","p12","p13","p14","p15","p16","p17","p18","p19","p20","p21","p22","p23","p24","p25","p26","p27","p28","p29","p30","p31"]
ff = ""

num = abs(number)
n_based = []
power = 0
dig = len(str(base))-1
if dig == 0:
    dig = 1
#print("dig=", dig)
#print(len(powers))

while num >= base:
    x = divmod(num, base)

    if x[1] == 0:
        n_based.append("0"*1)
    else:
        n_based.append(str(x[1]))
    num = x[0]
    power += 1
print(power)

    
if power >= len(powers):
    power2 = powers[-1]
    power = len(powers) - 1
else:
    power2 = powers[power]
   
    
n_based.append(str(num)) 
n_based.reverse()
n_str = "".join(n_based)

print("n_str", n_str)

if decimals == 0:
    core_n = str(round(int(n_str)//(10 ** (dig * power)), decimals))
    

else:
    nice_number = str(round(int(n_str)/(10 ** (dig * power)), decimals))
    core_n = nice_number.ljust(nice_number.find(".")+decimals+1, "0")

z = [core_n, power2, suffix]
print(core_n)


if number < 0:
    print("-"+"".join(z))
else:
    print("".join(z))
    

