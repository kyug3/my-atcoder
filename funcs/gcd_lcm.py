import math
from functools import reduce


def gcd(nums) -> int:
    return reduce(math.gcd, nums)
    
def lcm_base(a: int, b: int) -> int:
    return (a * b) // math.gcd(a, b)

def lcm(nums) -> int:
    return reduce(lcm_base, nums, 1)

def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = ext_gcd(b, a % b)
        x, y = y, x - a // b * y
        return x, y, g

# greatest common divisor
# least common multiple
