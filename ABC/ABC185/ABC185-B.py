import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
N_rest = N
last_B = 0
for _ in range(M):
    A, B = map(int, input().split())
    N_rest -= (A - last_B)
    if N_rest <= 0:
        print("No")
        exit()
    N_rest += (B - A)
    N_rest = min(N_rest, N)
    last_B = B

N_rest -= (T - last_B)
print("No" if N_rest <= 0 else "Yes")