import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

"""
試し割りは遅いので素因数分解のために割る数の候補を列挙しておきたい。
rの最大が大きいのでmin factorの列挙はできないが、√rまでが分かれば十分
(√r以上の素因数を2つ以上持つことはない)
[l, r]のそれぞれについて √r までの素因数の候補を区間篩の要領で列挙しておく
[l, r]のそれぞれを素因数の候補を用いて素因数分解していき、分解した回数をカウント
最後に1になっていなければ+1カウントし、カウントが素数か判定
"""
l, r = li()

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


def range_sieve_of_eratosthenes(A, B, primes):
    is_prime = [[] for _ in range(B - A + 1)]
    for p in primes:
        if p < A:
            start = A + (-A) % p
        else:
            start = p
        for i in range(start, B+1, p):
            is_prime[i-A].append(p)
    return is_prime

def factorization(x, ps):
    ret = []
    cnt = 0
    for p in ps:
        while x % p == 0:
            ret.append(p)
            cnt += 1
            x //= p
    if x > 1:
        cnt += 1
    return cnt

primes, is_prime = sieve_of_eratosthenes(10**5)
range_primes = range_sieve_of_eratosthenes(l, r, primes)

ans = 0
for i in range(l, r+1):
    cnt = factorization(i, range_primes[i-l])
    if is_prime[cnt]:
        ans += 1
print(ans)