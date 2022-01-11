import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N = int(input())
K = int(input())
x = li()
ans = 0
for i in range(N):
    ans += min(x[i], abs(K-x[i])) * 2
print(ans)