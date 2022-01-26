import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


N = int(input())
N *= 2
A = li() 
dp = [[INF] * N for _ in range(N)]
for i in range(N):
    for j in range(i+1):
        dp[i][j] = 0

for i in range(1, N, 2):
    for l in range(N-i):
        r = l + i
        dp[l][r] = dp[l+1][r-1] + abs(A[l] - A[r])
        for mid in range(l+1, r, 2):
            dp[l][r] = min(dp[l][r], dp[l][mid] + dp[mid+1][r])

print(dp[0][N-1])
