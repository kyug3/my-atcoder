import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

s = int(input())
def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

ans = []
se = set()
for i in range(1, 10**8):
    if i == 1:
        ans.append(s)
        se.add(s)
    else:
        x = f(ans[-1])
        if x in se:
            a = i
            break
        ans.append(x)
        se.add(x)
    
print(a)