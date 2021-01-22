import math
from typing import List, 
from functools import reduce


def gcd(nums: List[int]) -> int:
    return reduce(math.gcd, nums)

N = int(input())
A = list(map(int, input().split()))

print(gcd(A))