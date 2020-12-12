import sys
input = sys.stdin.readline

S = input().rstrip()
if S[0] == "S":
    print("Cloudy")
elif S[0] == "C":
    print("Rainy")
else:
    print("Sunny")