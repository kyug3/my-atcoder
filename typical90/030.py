import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

def sieve_of_eratosthenes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range (n + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, n+1, p):
            is_prime[i] = False

    return primes, is_prime


N, K = li()

primes, is_prime = sieve_of_eratosthenes(N+1)
count = [0] * (N+2)
for i in primes:
    for j in range(i, N+1, i):
        count[j] += 1

ans = 0
for i in count:
    if i >= K:
        ans += 1

print(ans)