import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import defaultdict

N = int(input())
A = li()
dic = defaultdict(int)
dic[0] = 1
ruiseki = [0]
ans = 0
for i in range(N):
    x = ruiseki[-1] + A[i]
    if x in dic:
        ans += dic[x]
    dic[x] += 1
    ruiseki.append(ruiseki[-1] + A[i])

print(ans)