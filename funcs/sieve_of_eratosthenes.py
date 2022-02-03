def sieve_of_eratosthenes(n):
    primes = []
    is_prime = [1] * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0

    for p in range (n + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, n+1, p):
            is_prime[i] = 0

    return primes


def range_sieve_of_eratosthenes(A, B, primes):
    # A以上B以下の整数について素数かどうか判定
    # A[i] : i+Aが整数かどうか
    # primesは √B 以下の素数のリスト
    is_prime = [1] * (B - A + 1)
    for p in primes:
        if p < A:
            start = A + (-A) % p
        else:
            start = p * 2
        for i in range(start, B+1, p):
            is_prime[i-A] = 0
    return is_prime