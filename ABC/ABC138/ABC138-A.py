import sys
input = sys.stdin.readline

a = int(input())
s = input().rstrip()
print(s if a >= 3200 else "red")