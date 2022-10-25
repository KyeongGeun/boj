import sys
sys.setrecursionlimit(10 ** 6)

dp: list


def recur(money, front, prev, idx):
    if idx == len(money) - 1:
        if not prev and not front:
            return money[-1]
        else:
            return 0

    if dp[front][prev][idx] != -1:
        return dp[front][prev][idx]

    ret = recur(money, front, False, idx + 1)
    if not prev:
        ret = max(ret, recur(money, front, True, idx + 1) + money[idx])

    dp[front][prev][idx] = ret
    return ret


def solution(money):
    global dp
    dp = [[[-1 for _ in range(len(money))]
           for _ in range(2)] for _ in range(2)]

    return max(recur(money, False, False, 1),
               recur(money, True, True, 1) + money[0])
