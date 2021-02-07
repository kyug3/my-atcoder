import math

N, M = map(int, input().split())
S = input()
T = input()

g = math.gcd(N, M)
lcm = N * M // g
for i in range(g):
    if S[i*N//g] != T[i*M//g]:
        print(-1)
        break
else:
    print(lcm)