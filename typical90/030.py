import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, K = li()

is_prime = [True] * (N+1)
count = [0] * (N+1)

for i in range(2, N+1):
    if not is_prime[i]:
        continue
    for j in range(i, N+1, i):
        count[j] += 1
        is_prime[j] = False

ans = 0
for i in count:
    if i >= K:
        ans += 1

print(ans)