import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

"""
カタラン数、経路問題に置き換えて考える
制約を無視した経路数から通れない経路を必ず通る経路数を引く
"""

N, M, K = li()

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
fif = enumfif(N+M+3, mod) 
 
def C(n, r):
    if n < 0 or r < 0 or r > n:
        return 0
    return fif[0][n] * fif[1][r] * fif[1][n-r] % mod

def P(n, r):
    return fif[0][n] * fif[1][n-r] % mod

if N > M + K:
    print(0)
    exit()

a = C(N+M, N)
tate = M + K + 1
yoko = N - K - 1
b = C(tate+yoko, yoko)
print((a - b) % mod)