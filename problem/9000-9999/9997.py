import sys
input = sys.stdin.readline

BI = (1 << 26) - 1


def check(start, bi):
    if bi == BI:
        return 2 ** (n - start)

    if start == n:
        return 0

    ans = 0
    ans += check(start + 1, bi)

    bi2 = bi | li[start]

    if bi != bi2:
        ans += check(start + 1, bi | li[start])
    else:
        ans *= 2

    return ans


n = int(input())


li = [0] * n

for i in range(n):
    s = input().rstrip()

    bi = 0
    for v in s:
        bi |= 2 ** (ord(v) - 97)

    li[i] = bi

print(check(0, 0))
