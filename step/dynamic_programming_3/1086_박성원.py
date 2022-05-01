from math import factorial, gcd
import sys
input = sys.stdin.readline

n = int(input())
li = [input().rstrip() for _ in range(n)]
intli = [int(li[i]) for i in range(n)]
k = int(input())
modli = [intli[i] % k for i in range(n)]

memo = [[-1 for _ in range(1 << n)] for _ in range(101)]
tenmemo = [1] * 51
tenmemo[0] %= k

for i in range(1, 51):
    tenmemo[i] = tenmemo[i - 1] * 10 % k


def func(num, bit):

    if bit == ((1 << n) - 1):
        if num % k == 0:
            return 1
        else:
            return 0

    if memo[num][bit] != -1:
        return memo[num][bit]

    cnt = 0
    for i in range(n):
        if bit & (1 << i) == 0:
            cnt += func((num * (tenmemo[len(li[i])]) +
                        modli[i]) % k, bit | (1 << i))

    memo[num][bit] = cnt
    return cnt


fu = func(0, 0)
fa = factorial(n)
g = gcd(fu, fa)
fu //= g
fa //= g
print(f'{fu}/{fa}')
