num = 1
num2 = 1
num3 =  0
l = list()
while(num3 < 4000000):
    num3 = num+num2
    if num3%2 == 0:
        l.append(num3)
    num = num2
    num2 = num3
print(sum(l))