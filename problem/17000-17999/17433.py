import sys
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return 0
    if a % b == 0:
        return b

    return gcd(b, a % b)


ans = []
for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))

    if n == 1:
        ans.append('INFINITY')
        continue

    g = li[1] - li[0]
    for i in range(2, len(li)):
        g = gcd(g, li[i] - li[i - 1])

    if g == 0:
        ans.append('INFINITY')
    else:
        ans.append(abs(g))

print(*ans, sep='\n')
