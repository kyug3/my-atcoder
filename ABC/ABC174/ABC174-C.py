import sys
input = sys.stdin.readline

K = int(input())
mod = 7 % K
if mod == 0:
    print(1)
    exit()
for n in range(2, K+1):
    mod = (mod * 10 + 7) % K
    if mod % K == 0:
        print(n)
        break
else:
    print(-1)