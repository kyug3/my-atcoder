import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())

ans = ''
while N != 0:
    if N % 2:
        N -= 1
        ans = '1' + ans
    else:
        ans = '0' + ans
    N //= -2
    
if ans == '':
    ans = '0'
print(ans)