s = input()

ans = 0
p = 0
for x in s:
    if x == 'g':
        if p:
            p -= 1
            ans += 1
        else:
            p += 1
    else:
        if p:
            p -= 1
        else:
            p += 1
            ans -= 1
print(ans)