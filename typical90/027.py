import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
s = set()
ans = []
for i in range(N):
    i += 1
    S = input().rstrip()
    if S in s:
        continue
    s.add(S)
    ans.append(i)
print(*ans)