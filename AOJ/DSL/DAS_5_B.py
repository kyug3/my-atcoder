import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
grid = [[0] * 1001 for _ in range(1001)]

for i in range(N):
    x1, y1, x2, y2 = li()
    grid[x1][y1] += 1
    grid[x1][y2] -= 1
    grid[x2][y1] -= 1
    grid[x2][y2] += 1

for j in range(1001-1):
    for i in range(1001):
        grid[i][j+1] += grid[i][j]

ans = 0
for i in range(1001-1):
    for j in range(1001):
        grid[i+1][j] += grid[i][j]
        ans = max(ans, grid[i+1][j])

ans = max(ans, max(grid[0]))
print(ans)