import math
from typing import List
from functools import reduce


def gcd(nums: List[int]) -> int:
    return reduce(math.gcd, nums)

N, X = map(int, input().split())
A = list(map(int, input().split()))

for n in range(N):
    A[n] = abs(A[n] - X)

print(gcd(A))