import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

H, W = li()
A = [li() for _ in range(H)]

Y = [0] * W
for w in range(W):
    count = 0
    for h in range(H):
        count += A[h][w]
    Y[w] = count

X = [0] * H
for h in range(H):
    count = 0
    for w in range(W):
        count += A[h][w]
    X[h] = count

ans = [[0] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        ans[h][w] = X[h] + Y[w] - A[h][w]

for x in ans:
    print(*x)