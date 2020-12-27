import math
from typing import List
from functools import reduce


def gcd(nums: List[int]) -> int:
    return reduce(math.gcd, nums)
    
def lcm_base(a: int, b: int) -> int:
    return (a * b) // math.gcd(a, b)

def lcm(nums: List[int]) -> int:
    return reduce(lcm_base, numbers, 1)

def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = ext_gcd(b, a % b)
        x, y = y, x - a // b * y
        return x, y, g

# greatest common divisor
# least common multiple


def my_gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return b

def my_gcd2(a, b):
    if b == 0:
        return a
    else:
        return my_gcd2(b, a % b)