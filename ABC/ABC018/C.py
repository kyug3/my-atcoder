import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

R, C, K = li()
grid = [input() for _ in range(R)]

ue = [[0] * C for _ in range(R)]
sita = [[0] * C for _ in range(R)]
left = [[0] * C for _ in range(R)]
right = [[0] * C for _ in range(R)]

for i in range(R):
    now = 0
    for j in range(C):
        if grid[i][j] == 'o':
            now += 1
        else:
            now = 0
        left[i][j] = now
    now = 0
    for j in range(C)[::-1]:
        if grid[i][j] == 'o':
            now += 1
        else:
            now = 0
        right[i][j] = now

for j in range(C):
    now = 0
    for i in range(R):
        if grid[i][j] == 'o':
            now += 1
        else:
            now = 0
        ue[i][j] = now
    now = 0
    for i in range(R)[::-1]:
        if grid[i][j] == 'o':
            now += 1
        else:
            now = 0
        sita[i][j] = now

ans = 0
for i in range(K-1, R-K+1):
    for j in range(K-1, C-K+1):
        if grid[i][j] == 'x':
            continue
        flag = True
        for k in range(1, K):
            if not (left[i+k][j] >= K-k and right[i+k][j] >= K-k):
                flag = False
            if not (left[i-k][j] >= K-k and right[i-k][j] >= K-k):
                flag = False
            if not (ue[i][j+k] >= K-k and sita[i][j+k] >= K-k):
                flag = False
            if not (ue[i][j-k] >= K-k and sita[i][j-k] >= K-k):
                flag = False
        if flag:
            ans += 1
print(ans)