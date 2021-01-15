x = int(input())
count = x // 11 * 2
x %= 11
if x > 6:
    count += 2
elif x > 0:
    count += 1
print(count)