import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
lst = []

for s in S:
    lst.append(s)
    if lst[-3:] == ['f', 'o', 'x']:
        lst.pop()
        lst.pop()
        lst.pop()
print(len(lst))