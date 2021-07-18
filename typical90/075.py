import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

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
balls = 0
for _, i in lst:
    balls += i

cnt = 1
if cnt >= balls:
    print(0)
    exit()
for i in range(1, N):
    cnt *= 2
    if cnt >= balls:
        break
print(i)