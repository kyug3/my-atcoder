import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))
ans = 0
for i in range(2**N):
    switch_on = []
    n = 0
    for j in range(N):
        if (i >> j) & 1:
            switch_on.append(j+1)
    for l in ks:
        count = 0
        for ll in l[1:]:
            if ll in switch_on:
                count += 1
        if count % 2 != p[n]:
            n += 1
            break
        n += 1
    else:
        ans += 1
print(ans)
