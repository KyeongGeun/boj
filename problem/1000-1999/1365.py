import sys
input = sys.stdin.readline


def bi_left(lis, v):
    l, r = 0, len(lis)

    while l < r:
        mid = (l + r) // 2
        if lis[mid] < v:
            l = mid + 1
        else:
            r = mid

    return l


n = int(input())
li = list(map(int, input().split()))

memo = [li[0]]

for i in range(1, n):
    if li[i] > memo[-1]:
        memo.append(li[i])
    else:
        l = bi_left(memo, li[i])
        memo[l] = li[i]

print(n - len(memo))
