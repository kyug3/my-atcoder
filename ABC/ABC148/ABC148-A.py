import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
lst = [1, 2, 3]
lst.remove(A)
lst.remove(B)
print(lst[0])