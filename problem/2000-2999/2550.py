from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

dic = {li2[i]: i for i in range(n)}
dic2 = {i: li2[i] for i in range(n)}

li1 = [dic[li1[i]] for i in range(n)]
li2 = [i for i in range(n)]

dp = [1] * (n)
li = [li1[0]]

for i in range(1, n):
    if li1[i] > li[-1]:
        li.append(li1[i])
        dp[i] = len(li)
    else:
        l = bisect_left(li, li1[i])
        li[l] = li1[i]
        dp[i] = l + 1

print(len(li))

ans = []
l = len(li)
for i in range(n - 1, -1, -1):
    if dp[i] == l:
        ans.append(dic2[li1[i]])
        l -= 1

        if l == 0:
            break

print(*sorted(ans))
