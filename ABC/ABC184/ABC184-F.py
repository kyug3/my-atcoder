import sys
import bisect
input = sys.stdin.readline

N, T = map(int, input().split())
A = list(map(int, input().split()))

left = A[:N//2]
right = A[N//2:]

lsum = []
for i in range(2 ** len(left)):
    count = 0
    for j in range(len(left)):
        if (i >> j) & 1:
            count += left[j]
    lsum.append(count)

rsum = []
for i in range(2 ** len(right)):
    count = 0
    for j in range(len(right)):
        if (i >> j) & 1:
            count += right[j]
    rsum.append(count)

rsum.sort()
ans = 0
for x in lsum:
    rest = T - x
    if rest < 0:
        continue
    pivot = bisect.bisect_right(rsum, rest)
    ans = max(ans, x + rsum[pivot-1])
print(ans)
