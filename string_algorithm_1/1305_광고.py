import sys
input = sys.stdin.readline


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


n = int(input())
s = input().rstrip()

pi = getPi(s)

print(len(s) - pi[-1])
