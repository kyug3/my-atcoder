def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for k in range(2, n + 1):
        if k ** 2 > n:
            break
        if n % k == 0:
            return False
    return True