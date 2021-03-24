N = int(input())
S = input()
wnum = S.count('W')
enum = S.count('E')

W = [0] * N # iより西の西向きの人数
E = [0] * N # iより東の東向きの人数
for i in range(N):
    if S[i] == 'E':
        enum -= 1
    E[i] = enum
    if S[N-1-i] == 'W':
        wnum -= 1
    W[N-1-i] = wnum

ans = 10 ** 9
for a, b in zip(W, E):
    ans = min(ans, a+b)
print(ans)