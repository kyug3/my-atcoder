import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    G[x-1].append(y-1)

memo = [-1 for _ in range(N)]
def dp(x):
    if not memo[x] == -1:
        return memo[x]
    count = 0
    for y in G[x]:
        count = max(count, dp(y) + 1)
    memo[x] = count
    return count

ans = 0
for n in range(N):
    ans = max(ans, dp(n))

print(ans)