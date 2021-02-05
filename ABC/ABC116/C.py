N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(101):
    flag = False
    for n in range(N):
        if H[n]:
            flag = True
            H[n] -= 1
        else:
            if flag:
                ans += 1
            flag = False
    else:
        if flag:
            ans += 1
print(ans)