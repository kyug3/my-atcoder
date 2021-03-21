S = input()
T = input()
ls = len(S)
lt = len(T)

for i in range(ls - lt + 1)[::-1]:
    tmp = S[:i] + T + S[i + lt:]
    for x, y in zip(S, tmp):
        if not (x == y or x == '?'):
            break
    else:
        break
else:
    print('UNRESTORABLE')
    exit()

ans = []
for x in tmp:
    if x == '?':
        ans.append('a')
    else:
        ans.append(x)

print(''.join(ans))