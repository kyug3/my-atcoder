N, M = map(int, input().split())
mod = 10 ** 9 + 7

if abs(N - M) > 1:
    print(0)
    exit()

d = 1
for i in range(1, N + 1):
    d *= i
    d %= mod

m = 1
for i in range(1, M + 1):
    m *= i
    m %= mod
ans = d * m % mod
if N == M:
    ans = ans * 2
    ans %= mod

print(ans)