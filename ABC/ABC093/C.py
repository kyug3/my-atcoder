import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

A, B, C = li()

ma = max((A, B, C))
if (ma * 3 - (A+B+C)) % 2 == 1:
    ma += 1
print((ma*3 - (A+B+C)) // 2)