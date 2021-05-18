import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

H, W = li()
def find(h, w):
    # xの根を求める
    if par[h][w] == [h, w]:
        return [h, w]
    else:
        par[h][w] = find(par[h][w][0], par[h][w][1])
        return par[h][w]

def union(x, y):
    # xとyが属する集合の併合
    x1 = find(x[0], x[1])
    x2 = find(y[0], y[1])
    if x1 == x2:
        return None
    par[x1[0]][x1[1]] = par[x2[0]][x2[1]]



par = [[[j, i] for i in range(W)] for j in range(H)]
seen = [[0] * W for _ in range(H)]
for _ in range(int(input())):
    q = li()
    if q[0] == 1:
        r, c = q[1], q[2]
        r -= 1
        c -= 1
        seen[r][c] = 1
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            i += r
            j += c
            if i < 0 or j < 0 or i >= H or j >= W:
                continue
            if seen[i][j] == 0:
                continue
            union((r, c), (i, j))
    else:
        a, b, c, d = q[1:]
        if (seen[a-1][b-1] == seen[c-1][d-1] == 1) and find(a-1,b-1) == find(c-1, d-1):
            print('Yes')
        else:
            print('No')
