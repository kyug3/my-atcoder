import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
K = int(input())

def f(cnt, now):
    if cnt == N:
        return now
    a1 = f(cnt+1, now*2)
    a2 = f(cnt+1, now+K)
    return min(a1, a2)

print(f(0, 1))