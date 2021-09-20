def get_divisors(x: int) -> list:
    divisors = []
    for i in range(1, x+1):
        if i * i > x:
            break
        if x % i == 0:
            divisors.append(i)
            if x // i != i:
                divisors.append(x // i)
    return divisors

print(get_divisors(5544))