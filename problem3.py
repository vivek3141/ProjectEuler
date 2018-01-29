import math


def isprime(n):
    for k in range(int(n/2)+1,1,-1):
        if n % k == 0:
            return False
    return True


num = 600851475143
for i in range(int(math.sqrt(num)),0,-1):
    if isprime(i):
        if num % i == 0:
            print(i)
            break