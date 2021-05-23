import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
grid = [[0] * (1001) for _ in range(1001)]
for _ in range(N):
    lx, ly, rx, ry = li()
    grid[ly][lx] += 1
    grid[ly][rx] -= 1
    grid[ry][lx] -= 1
    grid[ry][rx] += 1

for h in range(1001):
    for w in range(1, 1001):
        grid[h][w] += grid[h][w-1]

for w in range(1001):
    for h in range(1, 1001):
        grid[h][w] += grid[h-1][w]

ans = [0] * (N+1)
for h in range(1001):
    for w in range(1001):
        x = grid[h][w]
        if x > 0:
            ans[x] += 1

print(*ans[1:])
            