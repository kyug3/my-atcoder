import sys
import math
input = sys.stdin.readline

L = int(input())
print(
    math.factorial(L - 1)
    // (math.factorial(L - 1 - 11) * math.factorial(11))
)