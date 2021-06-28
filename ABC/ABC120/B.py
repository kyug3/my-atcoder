import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

A, B, K = li()
lst = []
ans = 1
while A >= ans and B >= ans:
    if A % ans == 0 and B % ans == 0:
        lst.append(ans)
    ans += 1
print(lst[-K])