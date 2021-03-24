A, B, C, D = list(input())

for i in range(2 ** 3):
    op = []
    for j in range(3):
        if (i >> j) & 1:
            op.append('+')
        else:
            op.append('-')
    result = A + op[0] + B + op[1] + C + op[2] + D
    if eval(result) == 7:
        print(result + "=7")
        break
