import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
A = [[] for _ in range(N)]
for i in range(1, N):
    b = int(input())
    b -= 1
    A[b].append(i)

memo = [0] * N
def f(x):
    if not A[x]:
        return 1
    if memo[x]:
        return memo[x]
    ma = INF * -1
    mi = INF
    for a in A[x]:
        y = f(a)
        ma = max(ma, y)
        mi = min(mi, y)
    memo[x] = ma + mi + 1
    return ma + mi + 1

print(f(0))   
