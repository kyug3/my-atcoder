import sys
import heapq
input = sys.stdin.readline

def func(x, y):
    return (x + y) / 2

N = int(input())
v = list(map(int, input().split()))
heapq.heapify(v)

for _ in range(N-1):
    x = heapq.heappop(v)
    y = heapq.heappop(v)
    heapq.heappush(v, func(x, y))

print(v[-1])