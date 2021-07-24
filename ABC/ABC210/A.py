import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, A, X, Y = li()

ans = 0
for i in range(1, N+1):
    if i <= A:
        ans += X
    else:
        ans += Y
print(ans)
