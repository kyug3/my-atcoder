import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
stri = ''

for s in S:
    stri += s
    try:
        if stri[-3:] == 'fox':
            stri = stri[:-3]
    except:
        pass
print(len(stri))
