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

A = sieve_of_eratosthenes(5555555)
print(len(A))