import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
ma = 0
idx = -1

for i in range(2, N+1):
    print('?', 1, i)
    sys.stdout.flush()
    l = int(input())
    if l > ma:
        ma = l
        idx = i

ans = ma
for i in range(1, N+1):
    if i == idx:
        continue
    print('?', i, idx)
    sys.stdout.flush() 
    l = int(input())
    ans = max(ans, l)
    
print('!', ans)