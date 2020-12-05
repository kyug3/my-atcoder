import sys
input = sys.stdin.readline

S = input().rstrip()
s1, s2 = S[:2], S[2:]

if int(s1) >= 13 or s1 == "00":
    if int(s2) >= 13 or s2 == "00":
        print("NA")
    else:
        print("YYMM")
else:
    if int(s2) >= 13 or s2 == "00":
        print("MMYY")
    else:
        print("AMBIGUOUS")