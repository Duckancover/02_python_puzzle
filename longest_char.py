a = "abbbbbbbbbbbbccccc"
res = 1
c = []
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        res += 1       
    else:
        res = 1
    c.append(res)
ans = max(c)
print(ans)