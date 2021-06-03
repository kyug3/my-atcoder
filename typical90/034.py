import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import defaultdict


N, K = li()
A = li()
dic = defaultdict(int)
left = 0
right = 0
ans = 0
for i in range(N):
    dic[A[i]] += 1
    right += 1
    if len(dic) > K:
        for j in range(left, N):
            dic[A[j]] -= 1
            if dic[A[j]] == 0:
                left = j+1
                del dic[A[j]]
                break

    ans = max(ans, right - left)

print(ans)