import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import defaultdict

N, M = li()
dic = defaultdict(int)
A = li()
ans = 0
ruiseki = [0]
for i in range(N):
    x = ruiseki[-1] + A[i]
    ruiseki.append(x)
    dic[x%M] += 1
    if A[i] % M == 0:
        ans += 1

for i in range(N-1):
    dic[ruiseki[i+1]%M] -= 1
    x = A[i] % M
    idx = M - x
    ans += dic[(ruiseki[i+1] + idx) % M]

print(ans)