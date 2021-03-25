from collections import defaultdict
S = input()
T = input()

s_dic = defaultdict(list)
t_dic = defaultdict(list)
for i in range(len(S)):
    s_dic[S[i]].append(i)
    t_dic[T[i]].append(i)

for l in s_dic.values():
    x = T[l[0]]
    for i in l[1:]:
        if x != T[i]:
            print('No')
            exit()

for l in t_dic.values():
    x = S[l[0]]
    for i in l[1:]:
        if x != S[i]:
            print('No')
            exit()

print('Yes')