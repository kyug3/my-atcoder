W = input()
dic = {}

for w in W:
    if w in dic:
        dic[w] += 1
    else:
        dic[w] = 1

for value in dic.values():
    if value % 2 == 1:
        print('No')
        break
else:
    print('Yes')