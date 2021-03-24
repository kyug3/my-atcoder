N = int(input())
T = list(map(int, input().split()))
tsum = sum(T)
M = int(input())
for _ in range(M):
    p, x = map(int, input().split())
    print(tsum - T[p - 1] + x)