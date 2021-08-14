import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, K = li()
P = li()
C = li()

lst = [[] for _ in range(N)]
for i in range(N):
    idx = i
    nxt = N+1
    while 1:
        if P[idx] - 1 == i:
            lst[i].append(C[i])
            break
        nxt = P[idx] - 1
        lst[i].append(C[nxt])
        idx = nxt

acc = [[0] for _ in range(N)]
for i in range(N):
    l = len(lst[i])
    for j in range(l):
        acc[i].append(acc[i][-1] + lst[i][j])

ans = -INF
for i in range(N):
    rui = [0]
    l = len(lst[i])
    if K >= l:
        ans = max(acc[i][-1] * (K//l), ans)
    for j in range(min(l, K)):
        y = K // l
        if y:
            if (j+1) <= (K % l):
                ans = max(ans, y * acc[i][-1] + acc[i][j+1])
            else:
                ans = max(ans, (y-1) * acc[i][-1] + acc[i][j+1])
        ans = max(acc[i][j+1], ans)
print(ans)
