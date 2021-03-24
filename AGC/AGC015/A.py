def is_ok(n, a, b):
    if a > b:
        print(0)
        return False
    elif a == b:
        print(1)
        return False
    elif n == 1 and a != b:
        print(0)
        return False
    else:
        return True
    
def main():
    N, A, B = map(int, input().split())
    if not is_ok(N, A, B):
        return 0
    print((N-2) * (B-A) + 1)
    return 0

main()