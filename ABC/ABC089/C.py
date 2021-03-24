N = int(input())
dic = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for _ in range(N):
    s = input()
    if s[0] in dic:
        dic[s[0]] += 1
lst = list(dic.values())
ans = 0
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += lst[i] * lst[j] * lst[k]
print(ans)