import sys
import math
import itertools
input = sys.stdin.readline

N = int(input())

def length(i, j):
    xi, yi = i[0], i[1]
    xj, yj = j[0], j[1]
    return math.sqrt(((xi - xj) ** 2) + ((yi - yj) ** 2))

lst = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for routes in itertools.permutations([n for n in range(N)]):
    for i in range(1, N):
        ans += length(lst[routes[i]], lst[routes[i-1]])

print(ans / math.factorial(N))