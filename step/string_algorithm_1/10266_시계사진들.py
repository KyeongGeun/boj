import sys
input = sys.stdin.readline
MOD = 360000


def getPi(s):
    m = len(s)
    j = 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]

        if s[i] == s[j]:
            j += 1
            pi[i] = j

    return pi


def kmp(s1, s2):
    n = len(s1)
    m = len(s2)
    pi = getPi(s2)
    j = 0
    for i in range(n):
        while j > 0 and s1[i] != s2[j]:
            j = pi[j - 1]

        if s1[i] == s2[j]:
            if j == m - 1:
                return True
            else:
                j += 1

    return False


n = int(input())
s = ['', '']

for idx in range(2):

    li = list(map(int, input().split()))

    cache = ['0'] * MOD

    for v in li:
        cache[v] = '1'

    s[idx] = ''.join(cache)

if kmp(s[0] + s[0], s[1]):
    print('possible')
else:
    print('impossible')
