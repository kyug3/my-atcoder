import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, C = li()
A = [[0] * (10**5+10) for _ in range(C+1)]
for _ in range(N):
    s, t, c = li()
    c -= 1
    A[c][s] += 1
    A[c][t] -= 1
lst = [0] * (10**5+10)
for i in range(C):
    for j in range(10**5+10):
        if A[i][j] < 0:
            lst[j+1] += A[i][j]
        else:
            lst[j] += A[i][j]
x = 0
ans = 1
for i in range(10**5+10):
    x += lst[i]
    ans = max(ans, x)

print(ans)