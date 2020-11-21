import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
stri = ''

for s in S:
    stri += s
    if stri[-3:] == 'fox':
        stri = stri[:-3]

print(len(stri))
