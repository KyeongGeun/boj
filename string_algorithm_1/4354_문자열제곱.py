import sys
input = sys.stdin.readline


def getPi(str):
    m = len(str)
    j = 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and str[i] != str[j]:
            j = pi[j - 1]

        if str[i] == str[j]:
            j += 1
            pi[i] = j

    return pi


while True:
    s = input().rstrip()
    if s == '.':
        break

    pi = getPi(s)
    l = len(s) - pi[-1]

    if pi[-1] == 0:
        print(1)
    else:
        if pi[-1] % l == 0:
            print(pi[-1] // l + 1)
        else:
            print(1)
