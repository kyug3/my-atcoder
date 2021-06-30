import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, K, P = li()
A = li()
if N == 1:
    if P >= A[0]:
        print(1)
    else:
        print(0)
    exit()
A1 = A[:N//2]
A2 = A[N//2:]

X = [[] for _ in range(N+1)]
for i in range(2 ** len(A1)):
    price = 0
    count = 0
    for j in range(len(A1)):
        if (i >> j) & 1:
            price += A1[j]
            count += 1
    X[count].append(price)


Y = [[] for _ in range(N+1)]
for i in range(2 ** len(A2)):
    price = 0
    count = 0
    for j in range(len(A2)):
        if (i >> j) & 1:
            price += A2[j]
            count += 1
    Y[count].append(price)

for i in range(len(Y)):
    Y[i] = sorted(Y[i])

import bisect
ans = 0
for i in range(len(X)): # i -> A1側の品物の数
    if K < i:
        break
    for a in X[i]:
        ans += bisect.bisect_left(Y[K-i], P-a+1)
print(ans)
