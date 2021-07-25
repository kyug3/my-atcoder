import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
W, H = li()
W -= 1; H -= 1

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

f, i = enumfif(H+W+1, mod)
print(C(H+W, W, mod, [f,i]))