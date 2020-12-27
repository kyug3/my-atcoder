import math

A, B = map(int, input().split())
g = math.gcd(A, B)

def factorization(x):
    lst = []
    if x == 1:
        lst.append(1)
        return lst
    
    for n in range(2, x + 1):
        if n ** 2 > x:
            break
        count = 0
        while x > 1 and x % n == 0:
            x //= n
            count += 1
        if count > 0:
            lst.append(n)
        if x == 1:
            break
    if x > 1:
        lst.append(x)

    return lst

lst = factorization(g)
if lst[0] == 1:
    print(1)
else:
    print(len(lst) + 1)