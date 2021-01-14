sx, sy, tx, ty = map(int, input().split())

ans = ''
ans += 'R' * abs(tx - sx) + 'U' * abs(ty - sy)
ans += 'L' * abs(tx - sx) + 'D' * abs(ty - sy)
ans += 'D' + 'R' * abs(tx - sx + 1) + 'U' * abs(ty - sy + 1) + 'L'
ans += 'U' + 'L' * abs(tx - sx + 1) + 'D' * abs(ty - sy + 1) + 'R'

print(ans)