import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import defaultdict

N = int(input())
dic = defaultdict(int)
for _ in range(N):
    dic[input().rstrip()] += 1

count = 0
ans = ''
for k, v in dic.items():
    if v > count:
        ans = k
        count = v
print(ans)
