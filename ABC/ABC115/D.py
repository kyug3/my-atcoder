import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, X = li()

# P           1
# B P P P B   5
# B BPPPB P BPPPB B   13
# B BBPPPBPBPPPBB P BBPPPBPBPPPBB B

A = [1]
P = [1]
for i in range(N):
    A.append(A[-1] * 2 + 3)
    P.append(P[-1] * 2 + 1)

def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + A[n-1]:
        return f(n-1, x-1)
    else:
        return P[n-1] + 1 + f(n-1, x-2-A[n-1])

ans = f(N, X)
print(ans)