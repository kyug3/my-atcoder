import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
A = li()
su = sum(A)
if su % N:
    print(-1)
    exit()

one = su // N
acc = 0
cnt = 0
ans = 0
for i in range(N):
    acc += A[i]
    cnt += 1
    if acc == cnt * one:
        acc = 0
        cnt = 0
    else:
        ans += 1
print(ans)