import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
rest = 0
for a in A:
    ans += (a + rest) // 2
    if a <= rest:
        rest = 0
    else:
        rest = (a+rest) % 2

print(ans)
