import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M = li()
AB = [li() for _ in range(N)]
AB.sort()

ans = 0
for a, b in AB:
    if M - b <= 0:
        ans += a * M
        break
    ans += a * b
    M -= b

print(ans)