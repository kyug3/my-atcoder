import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from itertools import permutations


s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()
l1 = len(s1)
l2 = len(s2)
l3 = len(s3)
se = set()
for s in (s1, s2, s3):
    for x in s:
        se.add(x)
if len(se) >= 11:
    print('UNSOLVABLE')
    exit()

for p in permutations(i for i in range(10)):
    dic = {i:j for i, j in zip(se, p)}
    flag = False
    if ((l1==1 and dic[s1[0]] == 0)
        or (l2==1 and dic[s2[0]] == 0)
        or (l3==1 and dic[s3[0]] == 0)):
        continue

    n1 = 0
    for i in range(l1-1):
        x = dic[s1[i]]
        if i == 0 and x == 0:
            flag = True
        n1 += x * (10**(l1-i-1))
    i = l1-1
    n1 += dic[s1[i]]

    n2 = 0
    for i in range(l2-1):
        x = dic[s2[i]]
        if i == 0 and x == 0:
            flag = True
        n2 += x * (10**(l2-i-1))
    i = l2-1
    n2 += dic[s2[i]]

    n3 = 0
    for i in range(l3-1):
        x = dic[s3[i]]
        if i == 0 and x == 0:
            flag = True
        n3 += x * (10**(l3-i-1))
    i = l3-1
    n3 += dic[s3[i]]

    if flag:
        continue
    if n3 == n1 + n2:
        print(n1)
        print(n2)
        print(n3)
        exit()
print('UNSOLVABLE')
