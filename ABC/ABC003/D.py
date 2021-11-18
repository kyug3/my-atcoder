import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

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

H, W = li()
X, Y = li() 
D, L = li()

f = enumfif(H*W, mod)

a = C(X*Y, D, mod, f) * C(X*Y - D, L, mod, f) % mod

b = C((X-1)*Y, D, mod, f) * C((X-1)*Y - D, L, mod, f) * 2 % mod
c = C(X*(Y-1), D, mod, f) * C(X*(Y-1) - D, L, mod, f) * 2 % mod

d = C((X-1)*(Y-1), D, mod, f) * C((X-1)*(Y-1) - D, L, mod, f) * 4 % mod
e = C(X*(Y-2), D, mod, f) * C(X*(Y-2) - D, L, mod, f) % mod
g = C((X-2)*Y, D, mod, f) * C((X-2)*Y - D, L, mod, f) % mod

h = C((X-1)*(Y-2), D, mod, f) * C((X-1)*(Y-2) - D, L, mod, f) * 2 % mod
i = C((X-2)*(Y-1), D, mod, f) * C((X-2)*(Y-1) - D, L, mod, f) * 2 % mod

if X <= 1 and Y <= 1:
    j = 0
else:
    j = C((X-2)*(Y-2), D, mod, f) * C((X-2)*(Y-2) - D, L, mod, f) % mod

k = (H-X+1) * (W-Y+1)
x = (a-b-c+d+e+g-h-i+j) * k % mod
print(x)