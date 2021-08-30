import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

X, Y = li()
if X >= Y:
    print(X-Y)
    exit()

from functools import lru_cache

@lru_cache(None)
def f(now, cnt):
    if now == X:
        return cnt
    if now + 1 == X or now - 1 == X:
        return cnt + 1
    if now < X:
        return cnt + X - now
    ret = now - X + cnt
    if now % 2 == 0:
        ret = min(f(now//2, cnt+1),  ret)
    ret = min(f((now+1) // 2, cnt+2), ret)
    ret = min(f((now-1) // 2, cnt+2), ret)
    return ret

print(f(Y, 0))