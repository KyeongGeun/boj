import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def recur(l, r, cnt, i):
    if l > r:
        return cnt
    if l == r:
        if s[l] == med[i]:
            cnt += 1
        return cnt
    if memo[l][r] != -1:
        return memo[l][r]

    ret = cnt
    if s[l] == med[i]:
        ret = max(ret, recur(l + 1, r, cnt + 1, (i + 1) % 3))
    if s[r] == med[i]:
        ret = max(ret, recur(l, r - 1, cnt + 1, (i + 1) % 3))

    memo[l][r] = ret
    return ret


n = int(input())
s = input().rstrip()
med = ('B', 'L', 'D')

length = 3 * n

memo = [[-1 for _ in range(length)] for _ in range(length)]

print(recur(0, length - 1, 0, 0))
