import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = li()
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

def f(x, p):
    b, w = 1, 1
    for y in G[x]:
        if y == p:
            continue
        b2, w2 = f(y, x)
        b *= w2
        w *= (b2 + w2)
        b %= mod
        w %= mod
    return b, w

b, w = f(0, -1)
print((b+w) % mod)
        