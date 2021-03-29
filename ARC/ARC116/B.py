mod = 998244353
N = int(input())
A = list(map(int, input().split()))
A.sort()
total = [0] * (N+1)
for i in range(1, N)[::-1]:
    total[i] = (2 * total[i+1] + A[i]) % mod

ans = 0
for i in range(N):
    ans += A[i] ** 2
    ans %= mod
    ans += total[i+1] * A[i]
    ans %= mod

print(ans)