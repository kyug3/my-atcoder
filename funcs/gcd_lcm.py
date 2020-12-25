import math
from typing import List
from functools import reduce


def gcd(nums: List[int]) -> int:
    return reduce(math.gcd, nums)
    
def lcm_base(x: int, y: int) -> int:
    return (x * y) // math.gcd(x, y)

def lcm(nums: List[int]) -> int:
    return reduce(lcm_base, numbers, 1)


# greatest common divisor
# least common multiple