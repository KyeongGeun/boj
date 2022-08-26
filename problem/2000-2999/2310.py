import sys
input = sys.stdin.readline

ans = []
while True:
    n = int(input())
    if n == 0:
        break

    li = [0] + [input().split()[:-1] for _ in range(n)]
    for i in range(1, n + 1):
        for j in range(1, len(li[i])):
            li[i][j] = int(li[i][j])

    money = [-1] * (n + 1)
    stack = []
    stack.append((0, 1))
    while stack:
        m, r = stack.pop()

        if m <= money[r]:
            continue
        money[r] = m

        if li[r][0] == 'L':
            m = max(m, li[r][1])
        elif li[r][0] == 'T':
            m -= li[r][1]
            if m < 0:
                continue

        if r == n:
            ans.append('Yes')
            break

        for i in range(2, len(li[r])):
            stack.append((m, li[r][i]))
    else:
        ans.append('No')

print('\n'.join(ans))
