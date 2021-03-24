import math
from functools import reduce
    
def lcm_base(a: int, b: int) -> int:
    return (a * b) // math.gcd(a, b)

def lcm(nums) -> int:
    return reduce(lcm_base, nums, 1)


N = int(input())
A = list(map(int, input().split()))
l = lcm(A)
ans = 0
for a in A:
    ans += ((l-1) % a)
print(ans)