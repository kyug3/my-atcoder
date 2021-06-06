import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, Q = li()
A = li()
c = 0
for _ in range(Q):
    t, x, y = li()
    x -= 1; y -= 1
    x = (x - c) % N
    y = (y - c) % N
    if t == 2:
        c += 1
    elif t == 1:
        A[x], A[y] = A[y], A[x]
    else:
        print(A[x])
