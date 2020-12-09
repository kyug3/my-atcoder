import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
count = 0
for n in range(N):
    if p[n] != n + 1:
        count += 1

if count <= 2:
    print("YES")
else:
    print("NO")