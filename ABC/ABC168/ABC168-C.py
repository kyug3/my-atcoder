import sys
import math
input = sys.stdin.readline

A, B, H, M = map(int, input().split())
angle = abs(((H * 30) + 30 * (M/60)) - M * 6)
angle = math.radians(min(angle, 360 - angle))
print(math.sqrt(A**2 + B**2 - (2*A*B* math.cos(angle))))
