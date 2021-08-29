import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

X = int(input())

ans = 1
for i in range(2, X+1):
    for j in range(2, X+1):
        if i ** j > X:
            break
        ans = max(ans, i**j)
print(ans)