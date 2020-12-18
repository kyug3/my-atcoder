from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

lst = list(permutations(sorted(P), N))
print(abs(lst.index(P) - lst.index(Q)))