import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
X, Y = [], []
XY = []
for _ in range(N):
    x, y = li()
    X.append(x)
    Y.append(y)
    XY.append((x, y))
X.sort()
Y.sort()
x = X[N//2]
y = Y[N//2]
ans = 0
for a, b in XY:
    ans += abs(a-x) + abs(b-y)
print(ans)