N = int(input())

def factorization(x):
    lst = []
    if x == 1:
        lst.append((1, 1))
        return lst
    
    for n in range(2, x + 1):
        if n ** 2 > x:
            break
        count = 0
        while x > 1 and x % n == 0:
            x //= n
            count += 1
        if count > 0:
            lst.append((n, count))
        if x == 1:
            break
    if x > 1:
        lst.append((x, 1))

    return lst

lst = factorization(N)
ans = [str(N) + ':']
for x, y in lst:
    for _ in range(y):
        ans.append(str(x))
print(*ans)
