import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N, Q = li()
ans = [0] * N
for _ in range(Q):
    l, r, t = li()
    for i in range(l-1, r):
        ans[i] = t

for a in ans:
    print(a)