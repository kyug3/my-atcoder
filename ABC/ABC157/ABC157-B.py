import sys
input = sys.stdin.readline

bingo = [list(map(int, input().split())) for n in range(3)]
N = int(input())
result = [[False for _ in range(3)] for _ in range(3)]
for _ in range(N):
    b = int(input())
    for n, r in enumerate(bingo):
        if b in r:
            result[n][r.index(b)] = True
ans = "No"
for i in range(3):
    if result[i][0] and result[i][1] and result[i][2]:
        ans = "Yes"
    elif result[0][i] and result[1][i] and result[2][i]:
        ans = "Yes"
if result[0][0] and result[1][1] and result[2][2]:
    ans = "Yes"
if result[0][2]and result[1][1] and result[2][0]:
    ans = "Yes"
print(ans)