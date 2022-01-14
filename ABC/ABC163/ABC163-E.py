import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N = int(input())
A = li()
A = [(A[i], i) for i in range(N)]
A.sort(reverse=True)

dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if i+j >= N:
            break
        a, idx = A[i+j]
        dp[i+1][j] = max(dp[i][j] + abs(idx - i) * a, dp[i+1][j])
        dp[i][j+1] = max(dp[i][j] + abs(idx - (N-j-1)) * a, dp[i][j+1])
ans = 0
for i in range(N+1):
    ans = max(ans, max(dp[i]))
print(ans)