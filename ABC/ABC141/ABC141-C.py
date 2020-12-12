import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
correct = [0 for _ in range(N)]
for _ in range(Q):
    Ai = int(input())
    correct[Ai - 1] += 1

ans = [K - (Q - x) for x in correct]
for x in ans:
    if x > 0:
        print("Yes")
    else:
        print("No")