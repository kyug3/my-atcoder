import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

grid = [input() for _ in range(4)]

f = lambda grid: list(zip(*grid[::-1]))
grid = f(grid)
grid = f(grid)

for g in grid:
    print(''.join(g))