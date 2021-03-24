S = input()

count1 = 0
count2 = 0
for i, s in enumerate(S):
    if i % 2 == 0 and s == '0':
        count1 += 1
    elif i % 2 == 1 and s == '1':
        count1 += 1

    if i % 2 == 1 and s == '0':
        count2 += 1
    elif i % 2 == 0 and s == '1':
        count2 += 1

print(min(count1, count2))