import math

N = int(input())
X = list(map(int, input().split()))

used = set()
prime = []
for i in range(2, 51):
    if i in used:
        continue
    prime.append(i)
    for j in range(i+1, 51):
        if j % i == 0:
            used.add(j)

M = len(prime)
ans = float('inf')
for i in range(1 << M):
    cnt = 1
    for j in range(M):
        if (i >> j) & 1:
            cnt *= prime[j]
    for x in X:
        if math.gcd(cnt, x) == 1:
            break
    else:
        ans = min(ans, cnt)
print(ans)
