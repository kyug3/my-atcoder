import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
T = [int(input()) for _ in range(N)]
ans = INF
for i in range(2 ** N):
    x, y = 0, 0
    for j in range(N):
        if (i >> j) & 1:
            x += T[j]
        else:
            y += T[j] 
    ans = min(ans, max(x, y))
print(ans)
