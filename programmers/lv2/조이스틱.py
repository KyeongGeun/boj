import sys
sys.setrecursionlimit(10 ** 6)


n: int


def changeAlpha(a):
    d = (ord(a) - ord('A')) % 26
    return min(d, abs(d - 26))


def changeLocation(a, b):
    return min(abs(a - b), abs(abs(a - b) - n))


def recur(cur, li, bit):
    ret = 500
    for i in range(len(li)):
        if bit & (1 << li[i]):
            continue
        ret = min(ret, recur(li[i], li, bit | (
            1 << li[i])) + changeLocation(cur, li[i]))

    if ret == 500:
        return 0
    return ret


def solution(name):
    global n
    n = len(name)

    answer = 0
    li = []
    for i, v in enumerate(name):
        if v != 'A':
            answer += changeAlpha(v)
            li.append(i)

    answer += recur(0, li, 1)

    return answer
