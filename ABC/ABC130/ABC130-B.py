import sys
input = sys.stdin.readline

N, X = map(int, input().split())
L = list(map(int, input().split()))
bound = [0]
for l in L:
    if bound[-1] + l <= X:
        bound.append(bound[-1] + l)
    else:
        break
print(len(bound))