import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

def get_table(k):
    modinv_table = [-1] * (k+1)
    modinv_table[1] = 1
    for i in range(2, k+1):
        modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod
    return modinv_table

def binomial_coefficients(n, k, modinv_table):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans


N, M, K = li()
t = get_table(N*M+1)
c = binomial_coefficients(N*M-2, K-2, t)

x = 0
for i in range(N):
    d = i * (N-i)
    x += d * c
    x %= mod
x *= M * M

y = 0
for i in range(M):
    d = i * (M-i)
    y += d * c
    y %= mod
y *= N * N

print((x+y) % mod)