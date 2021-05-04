import sys, math
from collections import deque, defaultdict
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

    return primes

N = int(input())
A = sieve_of_eratosthenes(55555)
ans = []
for i in A:
    if i % 5 == 1:
        ans.append(i)
        if len(ans) == N:
            break
print(*ans)