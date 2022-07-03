import sys
input = sys.stdin.readline


def calcu(s):
    if len(s) <= 2:
        if s in _set:
            return 1
        else:
            return 0

    s1 = s[0] + s[-1]
    s2 = ''.join(sorted(list(s[1:-1])))

    if s1 not in dic or s2 not in dic[s1]:
        return 0

    return dic[s1][s2]


dic = {}
_set = set()
for _ in range(int(input())):
    s = input().rstrip()

    if len(s) <= 2:
        _set.add(s)

    s1 = s[0] + s[-1]
    s2 = ''.join(sorted(list(s[1:-1])))

    if s1 not in dic:
        dic[s1] = {}

    if s2 not in dic[s1]:
        dic[s1][s2] = 0

    dic[s1][s2] += 1

ans = []
for _ in range(int(input())):
    li = input().split()

    num = 1
    for v in li:
        num *= calcu(v)

    ans.append(num)


print(*ans, sep='\n')
