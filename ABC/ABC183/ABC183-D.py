# Water Heater
import sys
input = sys.stdin.readline

N, W = map(int, input().rstrip().split())
lst = [0 for _ in range(2*(10**5)+1)]
 
for _ in range(N):
    s, t, p = map(int, input().rstrip().split())
    lst[s] += p
    lst[t] -= p
ans = 0
now = 0
for e in lst:
    now += e
    ans = max(ans, now)
 
if ans > W:
    print('No')
else:
    print('Yes')