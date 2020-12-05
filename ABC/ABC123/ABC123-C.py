import sys
import math
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(5)]

print(math.ceil(N / min(lst)) + 4)