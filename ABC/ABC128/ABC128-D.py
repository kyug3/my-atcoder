import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, K = li()
V = li()
ans = 0
for l in range(N+1):
    for r in range(N+1):
        if l + r > K or l + r > N:
            break
        lst = V[:l]
        if r:
            lst += V[-r:]
        lst.sort(reverse=True)
        for i in range(K-(l+r)):
            if lst and lst[-1] < 0:
                lst.pop()
            else:
                break
        if lst:
            ans = max(ans, sum(lst))
        
print(ans)
