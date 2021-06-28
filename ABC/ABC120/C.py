import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

S = list(input().rstrip())
lst = []
ans1 = 0
for s in S[::-1]:
    if lst and lst[-1] != s:
        ans1 += 1
        lst.pop()
    else:
        lst.append(s)
    
lst = []
ans2 = 0
for s in S:
    if lst and lst[-1] != s:
        ans2 += 1
        lst.pop()
    else:
        lst.append(s)

print(max(ans1, ans2) * 2)