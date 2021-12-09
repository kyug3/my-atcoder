import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


N, K = li()
ans = 0
lst = [0] * (K+1)
for i in range(1, K+1)[::-1]:
    x = pow(K//i, N, mod)
    for j in range(2*i, K+1, i):
        x -= lst[j]
        x %= mod
    ans += i * x
    lst[i] = x
    ans %= mod
print(ans)
