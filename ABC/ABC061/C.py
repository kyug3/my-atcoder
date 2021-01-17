import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort()
count = 0
for a, b in lst:
    count += b
    if count >= K:
        print(a)
        break