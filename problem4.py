ma = 0
for i in range(1000,99,-1):
    for k in range(1000, 99, -1):
        m = str(k*i)
        if ("".join(reversed(m)) == m) and (int(ma) < int(m)):
            ma = m
print(ma)
