import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, M = li()
lst = [[i] for i in range(N)]
for i in range(M):
    x, y = li()
    x -= 1; y -= 1
    lst[x].append(y)

dp = [0] * (2**N)
dp[0] = 1

for s in range(2**N):
    for i in range(N):
        ok = 1
        for j in lst[i]:
            if (s >> j) & 1:
                ok = 0
        if ok:
            dp[s | (1 << i)] += dp[s]

print(dp[-1])