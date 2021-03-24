N = int(input())
A = list(map(int, input().split()))

ans = 1
inc = False
dec = False
for n in range(N-1):
    if A[n] == A[n+1]:
        continue
    elif A[n] > A[n+1]:
        if dec:
            continue
        elif not inc:
            dec = True
        else:
            ans += 1
            inc = False
    else:
        if inc:
            continue
        elif not dec:
            inc = True
        else:
            ans += 1
            dec = False
print(ans)

