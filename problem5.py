def check(num):
    for i in range(2,21):
        if not ((num % i) == 0):
            return False
    return True


k = 20
while True:
    if check(k):
        print(k)
        break
    k += 1
