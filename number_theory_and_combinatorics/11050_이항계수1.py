def com(a, b):
    if b == 0:
        return 1
    elif a == b:
        return 1
    return com(a-1, b-1) + com(a-1, b)

n, k = map(int, input().split())

print(com(n, k))