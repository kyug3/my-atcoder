import sys
input = sys.stdin.readline

N = int(input())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))
AB.sort(key=lambda x: x[1])

time = 0
for a, b in AB:
    time += a
    if b < time:
        print("No")
        break
else:
    print("Yes")