import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))
def enumfif(n, mod):
    f = [0] * (n+1)
    invf = [0] * (n+1)
    f[0] = 1
    for i in range(1, n+1):
        f[i] = f[i-1] * i % mod
 
    a = f[n]
    b = mod
    p, q = 1, 0
    while b > 0:
        c = a//b
        d = a; a = b; b = d % b
        d = p; p = q; q = d-c*q
    invf[n] = p + mod if p < 0 else p
    for i in range(n-1,-1,-1):
        invf[i] = invf[i+1] * (i+1) % mod
    return f, invf
 
def C(n, r, mod, fif):
    if n < 0 or r < 0 or r > n:
        return 0
    return fif[0][n] * fif[1][r] * fif[1][n-r] % mod

fif = enumfif(10**6 + 1, mod)

H, W, A, B = li()

h = H-A
w = B+1
ans = 0
while h > 0 and w <= W:
    h2 = H-h
    w2 = W-w
    x = C(h+w-2, h-1, mod, fif)
    y = C(h2+w2, h2, mod, fif)
    ans += x * y
    ans %= mod
    h -= 1
    w += 1
print(ans % mod)