from collections import defaultdict

N, M = map(int, input().split())
dic = defaultdict(list)
for i in range(M):
    p, y = map(int, input().split())
    dic[p].append((i, y))

ans = [-1] * M
for k in dic.keys():
    dic[k].sort(key= lambda x: x[1])
    P = '0' * (6 - len(str(k))) + str(k)
    for i, j in enumerate(dic[k]):
        i += 1
        i = str(i)
        ans[j[0]] = P + ('0' * (6 - len(i)) + i)
        
print(*ans, sep='\n')