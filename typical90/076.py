import sys, math
#sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
A = li() * 2
t = sum(A) / 20
ans = 'No'
su = 0
start = -1
for i in range(2*N):
    if i - start > N:
        break
    su += A[i]
    if su == t:
        ans = 'Yes'
    while su > t and i > start:
        su -= A[start + 1]
        start += 1
print(ans)