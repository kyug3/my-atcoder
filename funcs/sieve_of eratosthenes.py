def sieve_of_eratosthenes(n):
    prime = [2]
    lst = [x for x in range(3, n + 1, 2)]
    while True:
        p = lst[0]
        if n <= p ** 2:
            return prime + lst
        prime.append(p)
        lst = [x for x in lst if x % p != 0]