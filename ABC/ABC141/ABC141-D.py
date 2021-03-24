import heapq
N, M = map(int, input().split())
A = [-n for n in list(map(int, input().split()))]

if N == 1:
    print(-A[0] // (2 ** M))
    exit()

heapq.heapify(A)
a = heapq.heappop(A)
b = heapq.heappop(A)
for _ in range(M):
    if a > b:
        b = -b // 2
        b = heapq.heappushpop(A, -b)
    else:
        a = -a // 2
        a = heapq.heappushpop(A, -a)
else:
    heapq.heappush(A, a)
    heapq.heappush(A, b)

print(-sum(A))