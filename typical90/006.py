import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))


N, K = li()
S = list(input().rstrip())
d = [deque([]) for _ in range(26)]

for e, s in enumerate(S):
    d[ord(s) - 97].append(e)

start = 0
ans = []
for i in range(N - K, N):
    flag = False
    for e, q in enumerate(d):
        while q:
            if start <= q[0] <= i:
                x = q.popleft()
                start = x+1
                flag = True
                break
            if start > q[0]:
                q.popleft()
            else:
                break
        if flag:
            break
    ans.append(chr(e + 97))
print(''.join(ans))