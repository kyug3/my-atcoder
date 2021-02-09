n, a, b = map(int, input().split())
mod = 10**9 + 7

def func(k):
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

t = func(b)
x = binomial_coefficients(n, a, t)
y = binomial_coefficients(n, b, t)
ans = pow(2, n, mod) - x - y - 1
print(ans % mod)