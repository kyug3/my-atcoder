import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

# d1 = m1 + m2
# d2 = m2 + m3
# d3 = m3 + m1
N = int(input())
A = li()
ans = [0] * N
# x = 山1の量
x = A[0] * 2 - A[1] * 2
for i in range(2, N):
    if i % 2 == 0:
        x += A[i] * 2
    else:
        x -= A[i] * 2
x //= 2
ans[0] = x
for i in range(1, N)[::-1]:
    ans[i] = A[i%N]*2 - ans[(i+1)%N]
print(*ans)