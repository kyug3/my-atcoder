import math
from functools import reduce

def lcm_base(x, y):
    return x * y // math.gcd(x, y)

def lcm(lst):
    return reduce(lcm_base, lst)

N = int(input())
a = list(map(int, input().split()))

print(lcm(a))