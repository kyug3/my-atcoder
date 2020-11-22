import sys
input = sys.stdin.readline

N = int(input())
seen = set()

for _ in range(N):
    seen.add(input())
print(len(seen))