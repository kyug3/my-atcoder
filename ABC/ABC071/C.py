N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

d = {}
x, y = 0, 0
frag = True
for a in A:
    if frag:
        if a in d:
            d[a] += 1
            if d[a] == 2:
                x = a
                frag = False
        else:
            d[a] = 1
    else:
        if a in d:
            d[a] += 1
            if d[a] == 2 or d[a] == 4:
                y = a
                break
        else:
            d[a] = 1
else:
    print(0)
    exit()
print(x * y)
