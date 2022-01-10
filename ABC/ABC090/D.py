import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N, K = li()
ans = 0
for b in range(K+1, N+1):
    for i in range(N+1):
        if i*b > N:
            break
        x = min(N-(i*b+K)+1, b-K)
        if K == 0 and i == 0 and x:
            x -= 1
        if x > 0:
            ans += x

print(ans)