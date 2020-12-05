import sys
import math
from functools import reduce
input = sys.stdin.readline

N = int(input())
lst = [n for n in range(1, N+1)]

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

print(lcm_list(lst) + 1)