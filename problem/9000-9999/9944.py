import sys
input = sys.stdin.readline


def dfs(x, y, c):
    if c == 0:
        return 0

    ret = float('inf')
    for i in range(4):
        cnt = 0
        a = x
        b = y
        while True:
            a += dx[i]
            b += dy[i]

            if a < 0 or a > n - 1:
                break
            if b < 0 or b > m - 1:
                break
            if brd[a][b] == '*':
                break
            if visited[a][b]:
                break
            visited[a][b] = True
            cnt += 1

        if cnt == 0:
            continue

        a -= dx[i]
        b -= dy[i]

        ret = min(ret, dfs(a, b, c - cnt))

        while cnt > 0:
            visited[a][b] = False
            a -= dx[i]
            b -= dy[i]
            cnt -= 1

    return ret + 1


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

ans = []
case = 1
while True:
    s = input()
    if not s:
        break

    n, m = map(int, s.split())
    visited = [[False for _ in range(m)] for _ in range(n)]

    brd = [input().rstrip() for _ in range(n)]

    cnt = -1
    for i in range(n):
        for j in range(m):
            if brd[i][j] == '.':
                cnt += 1

    mmin = float('inf')
    for i in range(n):
        for j in range(m):
            if brd[i][j] == '*':
                continue
            visited[i][j] = True
            mmin = min(mmin, dfs(i, j, cnt))
            visited[i][j] = False

    if mmin == float('inf'):
        ans.append(f"Case {case}: {-1 if mmin == float('inf') else mmin}")
    else:
        ans.append(f"Case {case}: {mmin}")

    case += 1

print('\n'.join(ans))
