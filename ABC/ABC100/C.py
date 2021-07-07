import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
A = li()
ans = 0
for a in A:
    while a % 2 == 0:
        a //= 2
        ans += 1

print(ans)