s = input()

b_count = 0
ans = 0
for x in s:
    if x == 'B':
        b_count += 1
    else:
        ans += b_count
    
print(ans)