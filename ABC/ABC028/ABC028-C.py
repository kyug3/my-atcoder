import sys
from itertools import combinations
input = sys.stdin.readline

inp = list(map(int, input().split()))
lst = []
for x in combinations(inp, 3):
    lst.append(sum(x))
lst.sort()
print(lst[-3])