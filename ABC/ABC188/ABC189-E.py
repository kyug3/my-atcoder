import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    G[x].append(y)

dp = [float('-inf')] * N
for i in range(N-1)[::-1]:
    for j in G[i]:
        dp[i] = max(dp[i], A[j])
        dp[i] = max(dp[i], dp[j])

ans = float('-inf')
for i in range(N):
    ans = max(ans, dp[i] - A[i])
print(ans)