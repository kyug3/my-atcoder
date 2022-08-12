import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

"""
最小値の最大化なので二分探索で解けないか考える

xについてソートしておくと、点iと距離がD以下の点が存在するかについて、
x_i+D < x_j (i<j)を満たす最小のjより右のyについて見ればよくなる。
xが大きい方からyの累積maxと累積minをとっておくことで、
尺取り法を使いO(N)で判定できるので、
距離について二分探索を含めてO(N log max(X))で解ける。
"""

N = int(input())

XY = [tuple(map(int, input().split())) for _ in range(N)]

XY.sort()
ymax = [-INF]
ymin = [INF]
for _, y in XY[::-1]:
    ymax.append(max(ymax[-1], y))
    ymin.append(min(ymin[-1], y))

ymax = ymax[1:][::-1]
ymin = ymin[1:][::-1]

def f(mid):
    r = 0
    for l in range(N):
        x, y = XY[l]
        while r < N and XY[r][0] - x <= mid:
            r += 1
        if r < N:
            dif = max(abs(ymax[r] - y), abs(ymin[r] - y))
            if dif > mid:
                return 0
    return 1

ok = 10**9+1
ng = -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
