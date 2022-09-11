import sys
input = sys.stdin.readline

n, b, c = map(int, input().split())
li = list(map(int, input().split()))

if c >= b:
    ans = 0
    for v in li:
        ans += v * b
    print(ans)
    exit(0)

ans = 0
for i in range(1, n - 1):
    if li[i] > li[i + 1]:
        temp = li[i] - li[i + 1]
        if li[i - 1] < temp:
            temp2 = temp - li[i - 1]
            ans += temp2 * b
            li[i] -= temp2
            temp -= temp2

        ans += temp * (b + c)

        li[i - 1] -= temp
        li[i] -= temp

    mmin = min(li[i - 1], li[i], li[i + 1])
    ans += mmin * (b + 2 * c)

    li[i - 1] -= mmin
    li[i] -= mmin
    li[i + 1] -= mmin

    if li[i - 1] > 0:
        ans += li[i - 1] * b
        li[i - 1] = 0

mmin = min(li[n - 2], li[n - 1])
ans += mmin * (b + c)
li[n - 1] -= mmin
li[n - 2] -= mmin

if li[n - 2] > 0:
    ans += li[n - 2] * b
else:
    ans += li[n - 1] * b

print(ans)
