import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

A, B = li()

grid = []
for i in range(50):
    grid.append(['#'] * 100)

for i in range(50):
    grid.append(['.'] * 100)

A -= 1; B -= 1
h = 0
w = 0
while A:
    grid[h][w] = '.'
    w += 2
    if w >= 100:
        h += 2
        w = 0
    A -= 1

h = 51
w = 0
while B:
    grid[h][w] = '#'
    w += 2
    if w >= 100:
        h += 2
        w = 0
    B -= 1

print(100, 100)
for a in grid:
    print(''.join(a))