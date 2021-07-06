import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
ans = 10**10
for i in range(1, N+1):
    j = N // i
    rest = N % i
    ans = min(abs(i - j) + rest, ans)
print(ans)