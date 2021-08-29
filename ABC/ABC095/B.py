import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, X = li()
M = [int(input()) for _ in range(N)]
ans = N
X -= sum(M)
ans += X // min(M)
print(ans)