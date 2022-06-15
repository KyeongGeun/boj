n, p, q, x, y = map(int, input().split())

memo = {}


def a(i):
    if i <= 0:
        return 1

    if i not in memo:
        memo[i] = a(i // p - x) + a(i // q - y)

    return memo[i]


print(a(n))
