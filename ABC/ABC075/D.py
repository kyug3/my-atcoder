import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, K = li()
XY = []
X = []
Y = []
for _ in range(N):
    x, y = li()
    XY.append((x, y))
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
ans = float('inf')
for i in range(N):
    for j in range(i+1, N):
        for k in range(N):
            for l in range(k+1, N):
                xmin = X[i]
                xmax = X[j]
                ymin = Y[k]
                ymax = Y[l]
                count = 0
                for x, y in XY:
                    if xmin <= x <= xmax and ymin <= y <= ymax:
                        count += 1
                if count >= K:
                    area = abs(xmax - xmin) * abs(ymax - ymin)
                    ans = min(area, ans)
print(ans)