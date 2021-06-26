import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

# K % 2 == 0 なら
# a mod K = K // 2
# b mod K = K // 2
# c mod K = K // 2
# or 全部 mod K = 0

N, K = li()
ans = 0
x = N // K
ans += x ** 3
if K % 2:
    print(ans)
    exit()

count = 0
for i in range(1, N+1):
    if i % K == K//2:
        count += 1
if count:
    ans += count ** 3
print(ans)