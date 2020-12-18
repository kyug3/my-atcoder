N, M = map(int, input().split())
AC = [0 for _ in range(N)]
WA = [0 for _ in range(N)]

for _ in range(M):
    p, s = input().split()
    p = int(p) - 1
    if s == "AC":
        AC[p] = 1
    else:
        if AC[p] == 0:
            WA[p] += 1

for n in range(N):
    if WA[n] > 0 and AC[n] == 0:
        WA[n] = 0

print(sum(AC), sum(WA))