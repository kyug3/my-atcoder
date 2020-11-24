import sys
input = sys.stdin.readline

N = int(input())
last_t, last_x, last_y = 0, 0, 0
for n in range(N):
    t, x, y = map(int, input().split())
    dif_t = t - last_t
    dif_t -= (abs(x - last_x) + abs(y - last_y))
    if dif_t >= 0 and dif_t % 2 == 0:
        last_t, last_x, last_y = t, x, y
    else:
        print('No')
        break
else:
    print('Yes')
