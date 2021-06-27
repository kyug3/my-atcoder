import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

S = input().rstrip()
K = int(input())
cnt = 0
for s in S:
    if not s == '1':
        ans = int(s)
        break
    else:
        cnt += 1
        if cnt == K:
            ans = 1
            break
else:
    ans = 1
print(ans)