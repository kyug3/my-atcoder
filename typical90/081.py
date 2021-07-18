import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, K = li()
ma = 5005
data = [[0] * (ma+10) for _ in range(ma+10)]
for _ in range(N):
    a, b = li()
    data[a][b] += 1

for h in range(ma):
    for w in range(1, ma):
        data[h][w] += data[h][w-1]

for w in range(ma):
    for h in range(1, ma):
        data[h][w] += data[h-1][w]

ans = 0
for h in range(1, ma-K):
    for w in range(1, ma-K):
        x = data[h+K][w+K] - data[h-1][w+K] - data[h+K][w-1] + data[h-1][w-1]
        ans = max(ans, x)
print(ans)
