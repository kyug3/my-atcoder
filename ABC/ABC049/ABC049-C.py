S = list(input())
T = ''
s = set(['maerd', 'remaerd', 'esare', 'resare'])

while S:
    T += S.pop()
    if len(T) >= 5:
        if T in s:
            T = ''
    if len(T) >= 8:
        break
ans = 'YES' if T == '' else 'NO'
print(ans)