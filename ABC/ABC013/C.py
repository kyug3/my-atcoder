import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, H = li()
A, B, C, D, E = li()

def check(x):
    return B * x + D * (i-x) + H - (E*(N-i)) > 0


ans = INF
for i in range(N+1):
    ok = i + 1
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    if ok <= i:
        ans = min(ans, ok*A + (i-ok)*C)
print(ans)