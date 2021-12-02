import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))
from copy import deepcopy
from functools import lru_cache

B = [li() for _ in range(2)]
C = [li() for _ in range(3)]

@lru_cache(None)
def f(masu, turn):
    if turn == 9:
        x, y = 0, 0
        for i in range(2):
            for j in range(3):
                idx = i*3 + j
                if masu[idx] == masu[idx + 3]:
                    x += B[i][j]
                else:
                    y += B[i][j]
        for i in range(3):
            for j in range(2):
                idx = i*3 + j
                if masu[idx] == masu[idx+1]:
                    x += C[i][j]
                else:
                    y += C[i][j]
        return x, y
    
    x, y = -1, -1
    masu = list(masu)
    for i in range(3):
        for j in range(3):
            idx = i*3 + j
            if masu[idx] == -1:
                m = deepcopy(masu)
                m[idx] = turn % 2
                rx, ry = f(tuple(m), turn+1)
                if turn % 2:
                    if ry > y:
                        x, y = rx, ry
                else:
                    if rx > x:
                        x, y = rx, ry
    return x, y

M = tuple(-1 for _ in range(9))
a, b = f(M, 0)
print(a)
print(b)