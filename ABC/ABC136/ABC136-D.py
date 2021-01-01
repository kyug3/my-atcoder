S = input()
result = [0 for _ in range(len(S))]
last = 'R'
r_count = 0
l_count = 0
for n, s in enumerate(S):
    if s == 'R':
        if last == 'R':
            r_count += 1
        else:
            result[remind - 1] = (r_count + 1) // 2 + l_count // 2
            result[remind] = r_count // 2 + (l_count + 1) // 2
            r_count = 1
            l_count = 0
    else:
        if last == 'L':
            l_count += 1
        else:
            remind = n
            l_count += 1
    last = s
else:
    result[remind - 1] = (r_count + 1) // 2 + l_count // 2
    result[remind] = r_count // 2 + (l_count + 1) // 2

print(*result)