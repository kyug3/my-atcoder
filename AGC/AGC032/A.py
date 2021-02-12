N = int(input())
B = list(map(int, input().split()))
ans = []

if N == 1:
    print(1)
    exit()

lastlen = N
while B:
    lb = len(B)
    if lb == len(set(B)) == B[-1]:
        for b in B[::-1]:
            ans.append(b)
        break
    if B[-1] == lb:
        ans.append(lb)
        del B[-1]
        continue
    for i in range(0, lb)[::-1]:
        if B[i-1] == i:
            if B[i] > i:
                continue
            del B[i-1]
            ans.append(i)
            break
    if len(B) == lastlen:
        print(-1)
        exit()
    lastlen = len(B)

for x in ans[::-1]:
    print(x)