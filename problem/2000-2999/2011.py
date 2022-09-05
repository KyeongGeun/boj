import sys
sys.setrecursionlimit(10 ** 6)

MOD = 1000000


def func(idx):
    if idx > len(li) - 1:
        return 1
    if memo[idx] != -1:
        return memo[idx]

    if li[idx] < 3 and idx != len(li) - 1 and (li[idx] == 1 or li[idx + 1] < 7):
        ret = func(idx + 1) + func(idx + 2)
    else:
        ret = func(idx + 1)

    memo[idx] = ret % MOD
    return memo[idx]


li = list(map(int, list(input())))

memo = [-1] * len(li)

for i in range(len(li)):
    if li[i] == 0:
        memo[i] = 0

print(func(0))
