import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))
import bisect

N = int(input())
A = li()
G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = li()
    u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

seen = [0] * N
ans = [0] * N
def func(x, lis):
    idx = bisect.bisect_left(lis, A[x])
    if idx == len(lis):
        f = 1
        lis.append(A[x])
    else:
        f = 2
        ori = lis[idx]
        lis[idx] = A[x]
    ans[x] = len(lis)
    seen[x] = 1
    for y in G[x]:
        if seen[y]:
            continue
        func(y, lis)
    if f == 1:
        lis.pop()
    elif f == 2:
        lis[idx] = ori

func(0, [])
for a in ans:
    print(a)