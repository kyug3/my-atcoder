import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
INF = float('inf')

N, M = li()

keys = []
for _ in range(M):
    a, b = li()
    C = set(map(int, input().split()))
    keys.append([C, a])

dp = [INF] * (2**N)
dp[0] = 0
for s in range(2**N):
    for i in range(M):
        c, a = keys[i]
        tmp = 0
        for j in c:
            tmp |= 1 << (j-1)
        dp[s|tmp] = min(dp[s|tmp], dp[s] + a)
if dp[-1] == INF:
    ans = -1
else:
    ans = dp[-1]
print(ans)