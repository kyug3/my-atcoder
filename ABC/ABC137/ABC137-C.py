import sys
import math
input = sys.stdin.readline

N = int(input())
dic = {}
ans = 0
for _ in range(N):
    x = ''.join(sorted(list(input().rstrip())))
    if x in dic:
        ans += dic[x]
        dic[x] += 1
    else:
        dic[x] = 1

print(ans)