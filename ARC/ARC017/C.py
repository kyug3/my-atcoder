import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import defaultdict

N, X = li()
W = [int(input()) for _ in range(N)]
W1 = W[:N//2]
W2 = W[N//2:]

dic1 = defaultdict(int)
for i in range(2 ** len(W1)):
    count = 0
    for j in range(len(W1)):
        if (i >> j) & 1:
            count += W1[j]
    dic1[count] += 1

dic2 = defaultdict(int)
for i in range(2 ** len(W2)):
    count = 0
    for j in range(len(W2)):
        if (i >> j) & 1:
            count += W2[j]
    dic2[count] += 1

ans = 0
for k, v in dic1.items():
    ans += dic2[X-k] * v

print(ans)