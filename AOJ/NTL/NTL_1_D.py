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

def phi(x):
    nums = factorization(x)
    for n in nums:
        x *= 1 - 1 / n
    return int(x)

N = int(input())
print(phi(N))