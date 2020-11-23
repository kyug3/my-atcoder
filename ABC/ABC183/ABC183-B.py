import sys
input = sys.stdin.readline

def x(y):
    return ((gx - sx)*(y - sy) + gy*sx - sy*sx) / (gy - sy)

sx, sy, gx, gy = map(int, input().split())
gy *= -1

print(x(0))