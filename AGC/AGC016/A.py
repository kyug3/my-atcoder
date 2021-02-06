s = input()

if len(set(s)) == 1:
    print(0)
    exit()

for i in range(1, len(s)):
    for j in range(len(s)-i+1):
        x = set(s[j: j+i])
        if j == 0:
            se = x
        elif not x & se:
            break
        else:
            se &= x
    else:
        print(i-1)
        exit()
