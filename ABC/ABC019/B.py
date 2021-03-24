s = input()
ans = []

now = s[0]
cnt = 1
for i in range(1, len(s)):
    if s[i] == now:
        cnt += 1
    else:
        ans.append(now + str(cnt))
        cnt = 1
        now = s[i]

ans.append(now + str(cnt))
print(''.join(ans))