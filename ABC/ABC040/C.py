import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
A = [0] + li()
dp = [10**10] * (N+1)
dp[1] = 0
for i in range(1, N):
    dp[i+1] = min(dp[i+1], dp[i] + abs(A[i] - A[i+1]))
    if i + 2 < N+1:
        dp[i+2] = min(dp[i+2], dp[i]+ abs(A[i] - A[i+2]))
print(dp[-1])
