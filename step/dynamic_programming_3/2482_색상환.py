import sys
input = sys.stdin.readline

MOD = 1_000_000_003
N = int(input())
K = int(input())

memo = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]


def func(n, k):

    if n < 0 or k < 0:
        return 0
    if memo[n][k] != -1:
        return memo[n][k]
    if n == 0 or k == 1:
        return n
    if k == 0:
        return 1
    if n + 1 < k * 2:
        return 0

    memo[n][k] = (func(n - 1, k) + func(n - 2, k - 1)) % MOD

    return memo[n][k]


if K == 1:
    print(N)
elif N == K * 2:
    print(2)
elif N < K * 2:
    print(0)
else:
    print((func(N - 1, K) + func(N - 3, K - 1)) % MOD)
