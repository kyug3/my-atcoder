import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = [0] + A + [N + 1]
white = []
k = float("inf")
for m in range(M+1):
    dif = A[m + 1] - A[m] - 1
    if dif <= 0:
        continue
    white.append(dif)
    k = min(k, dif)

ans = 0
for w in white:
    ans += math.ceil(w / k)
print(ans)