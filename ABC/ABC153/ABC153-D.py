import math
H = int(input())
ans = 0
phase = 1
while True:
    H = H // 2
    ans += phase
    phase *= 2
    if H < 1:
        break
print(ans)