import sys
import math
input = sys.stdin.readline

N = int(input())
T = input().rstrip()

x = math.ceil(N / 3)
part_t = "110" * x
if not T in part_t:
    x += 1
    part_t += "110"
count = 0
for i in range(N, len(part_t)+1):
    if part_t[i - N: i] == T:
        count += 1

print((10**10 - x + 1) * count)