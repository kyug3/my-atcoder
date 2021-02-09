"""
def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10 ** 9 + 7
N = 10 ** 4
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod//i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

a = cmb(n, r, mod)
"""
# ABC156 D
n, a, b = map(int, input().split())
mod = 10**9 + 7

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

t = get_table(b)
x = binomial_coefficients(n, a, t)
y = binomial_coefficients(n, b, t)
ans = pow(2, n, mod) - x - y - 1
print(ans % mod)