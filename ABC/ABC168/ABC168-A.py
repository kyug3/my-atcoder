import sys
input = sys.stdin.readline

N = input().rstrip()
pon = ["0", "1", "6", "8"]
if N[-1] == "3":
    print("bon")
elif N[-1] in pon:
    print("pon")
else:
    print("hon")