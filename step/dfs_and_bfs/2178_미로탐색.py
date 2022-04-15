import sys
input = sys.stdin.readline

def bfs(x, y):

    q = [(x, y)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q[0][0], q[0][1]
        del q[0]
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < n and 0 <= b < m and li[a][b] == '1':
                li[a][b] = li[x][y] + 1
                q.append((a, b))

n, m = map(int, input().split())

li = [list(input().rstrip()) for _ in range(n)]

li[0][0] = 1
bfs(0, 0)
print(li[n - 1][m - 1])