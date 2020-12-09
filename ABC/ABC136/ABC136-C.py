import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
now_max = 0
for n in range(N):
    if now_max > H[n]:
        print('No')
        break
    now_max = max(now_max, H[n] - 1)
else:
    print('Yes')
