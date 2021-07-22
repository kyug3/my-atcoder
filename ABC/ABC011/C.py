import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
dp = [INF] * (N+1)
dp[-1] = 0
for _ in range(3):
    ng = int(input())
    if ng <= N:
        dp[ng] = -1

for i in range(N+1)[::-1]:
    if dp[i] == -1:
        continue
    for j in range(1, 4):
        if i - j < 0: continue
        if dp[i-j] == -1: continue
        dp[i-j] = min(dp[i-j], dp[i] + 1)

if dp[0] <= 100:
    print('YES')
else:
    print('NO')