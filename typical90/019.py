import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))
from functools import lru_cache

N = int(input())
A = li() 

@lru_cache(None)
def f(L, R):
    if L == R:
        return 0
    ret = INF
    for r in range(L+1, R, 2):
        x = abs(A[L] - A[r]) + f(L+1, r) + f(r+1, R)
        ret = min(x, ret)
    return ret

print(f(0, 2*N))