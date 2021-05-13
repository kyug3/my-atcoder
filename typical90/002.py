import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
s = set()
for i in range(2 << N):
    lst = []
    for j in range(N):
        if (i >> j) & 1:
            lst.append('(')
        else:
            lst.append(')')
    s.add(''.join(lst))

ans = []
for x in s:
    count0 = 0
    count1 = 0
    flag = False
    for i in range(N):
        if x[i] == ')':
            count0 += 1
        else:
            count1 += 1
        if count0 > count1:
            flag = True
            break
    if flag or count0 != count1:
        continue
    ans.append(x)
ans.sort()
print(*ans)