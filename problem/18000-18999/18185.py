import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

ans = 0
for i in range(1, n - 1):
    if li[i] > li[i + 1]:
        temp = li[i] - li[i + 1]
        if li[i - 1] < temp:
            temp2 = temp - li[i - 1]
            ans += temp2 * 3
            li[i] -= temp2
            temp -= temp2

        ans += temp * 5

        li[i - 1] -= temp
        li[i] -= temp

    mmin = min(li[i - 1], li[i], li[i + 1])
    ans += mmin * 7

    li[i - 1] -= mmin
    li[i] -= mmin
    li[i + 1] -= mmin

    if li[i - 1] > 0:
        ans += li[i - 1] * 3
        li[i - 1] = 0

mmin = min(li[n - 2], li[n - 1])
ans += mmin * 5
li[n - 1] -= mmin
li[n - 2] -= mmin

if li[n - 2] > 0:
    ans += li[n - 2] * 3
else:
    ans += li[n - 1] * 3

print(ans)
