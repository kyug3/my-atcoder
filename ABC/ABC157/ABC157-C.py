import sys
input = sys.stdin.readline

N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]
ans = [-1 for _ in range(N)]

for sc in SC:
    s, c = sc[0], sc[1]
    if ans[s-1] == -1 or ans[s-1] == c:
        ans[s-1] = c
    else:
        print(-1)
        exit()
if ans[0] == 0 and N > 1:
    print(-1)
    exit()

for n in range(len(ans)):
    if ans[n] == -1:
        if n == 0 and N > 1:
            ans[n] = 1
        else:
            ans[n] = 0
print("".join(map(str, ans)))