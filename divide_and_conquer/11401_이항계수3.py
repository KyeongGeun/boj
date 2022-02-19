# 페르마 소정리
# a**(p-1) = 1 (mod p) (a: 정수, p: 소수, a%p != 0)
# a**(p-2) = a**(-1) (mod p)

import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def facto(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
        ans %= MOD
    return ans

def pow(a, n):
    if n == 0:
        return 1

    ans = pow(a, n//2) ** 2 % MOD

    if n%2 != 0:
        ans *= a
        ans %= MOD

    return ans

n, k = map(int, input().split())
print(facto(n) * pow(facto(n-k) * facto(k), MOD-2) % MOD)