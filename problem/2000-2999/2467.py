import sys
input = sys.stdin.readline


def bi(x, l, r):
    while l < r:
        mid = (l + r) // 2

        if li[mid] < -x:
            l = mid + 1
        else:
            r = mid

    return l


n = int(input())

li = list(map(int, input().split()))

mmin = abs(li[0] + li[n - 1])
ans = li[0], li[n - 1]

for i in range(n - 1):
    x = bi(li[i], i + 1, n - 1)

    ab = abs(li[i] + li[x])
    if ab < mmin:
        mmin = ab
        ans = li[i], li[x]

        if mmin == 0:
            break

    if x - 1 == i:
        continue

    ab = abs(li[i] + li[x - 1])
    if ab < mmin:
        mmin = ab
        ans = li[i], li[x - 1]

        if mmin == 0:
            break

print(*ans)
