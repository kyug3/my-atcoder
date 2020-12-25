import math
from functools import reduce

N = int(input())
T = []
for n in range(N):
    T.append(int(input()))

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

print(lcm(*T))