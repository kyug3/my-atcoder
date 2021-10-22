import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
#mod = 10**9 + 7
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

def ext_gcd(a, b):
    """
    ax + by = gcd(a,b)
    を満たす gcd(a,b), x, y
    """
    if a == 0:
        return b, 0, 1
    g, y, x = ext_gcd(b % a, a)
    return g, x - (b // a) * y, y

H, W, K = li()
dp = [[0] * (W+1) for _ in range(H+1)]
dp[0][0] = pow(3, (H*W - K), mod)
_, x, _ = ext_gcd(3, mod)
grid = [[0] * (W+1) for _ in range(H+1)]
for _ in range(K):
    h, w, c = input().split()
    h = int(h) - 1; w = int(w) - 1
    grid[h][w] = c

dp[0][0] = pow(3, (H*W - K), mod)

def check_next(h, w, dh, dw):
    if grid[dh][dw] == 0:
        dp[dh][dw] += dp[h][w] * x
    else:
        dp[dh][dw] += dp[h][w]
    dp[dh][dw] %= mod

for h in range(H):
    for w in range(W):
        if grid[h][w] == 0:
            check_next(h, w, h+1, w)
            check_next(h, w, h+1, w)
            check_next(h, w, h, w+1)
            check_next(h, w, h, w+1)
        elif grid[h][w] == 'X':
            check_next(h, w, h+1, w)
            check_next(h, w, h, w+1)
        elif grid[h][w] == 'R':
            check_next(h, w, h, w+1)
        else:
            check_next(h, w, h+1, w)
print(dp[H-1][W-1])
print(5000*5000)