def get_divisors(x: int) -> list:
    divisors = []
    for i in range(1, x):
        if i * i > x:
            break
        if x % i == 0:
            divisors.append(i)
            divisors.append(x // i)
    divisors = list(set(divisors))
    return divisors

print(get_divisors(4))