import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, X, M = li()
ans = 0
l = []
b = [0] * (M+1)
for i in range(N):
    if b[X] == 1:
        l.append(X)
    if b[X] == 2:
        count = i
        break
    ans += X
    b[X] += 1
    X **= 2
    X %= M
else:
    print(ans)
    exit()

N -= count
rest = N % len(l)
ans += sum(l[:rest])
for x in l:
    ans += x * (N//len(l))
print(ans)