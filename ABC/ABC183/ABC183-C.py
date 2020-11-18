# Travel
import sys
import itertools
input = sys.stdin.readline

N, K = map(int, input().split())
T  = [list(map(int, input().split())) for _ in range(N)]
 
lst = [n for n in range(2, N+1)]
ans = 0
for route in itertools.permutations(lst, len(lst)):
    route = [1] + list(route) + [1]
    counter = 0
    for n in range(N):
        counter += T[route[n] - 1][route[n+1] - 1]
    if counter == K:
        ans += 1

print(ans)