S = input()

lst = []
for s in S:
    if s == 'B':
        if lst:
            lst.pop()
    else:
        lst.append(s)
print(''.join(lst))