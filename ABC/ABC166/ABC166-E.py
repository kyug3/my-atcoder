import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import defaultdict

# j - A[j]== A[i] + i (i < j)
N = int(input())
A = li()
dic = defaultdict(int)
for i in range(N):
    dic[i+A[i]] += 1
ans = 0
for j in range(N)[::-1]:
    ans += dic[j-A[j]]

print(ans)