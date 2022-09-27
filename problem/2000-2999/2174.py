import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())

dic = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
robot = [[] for _ in range(n + 1)]

brd = [[0 for _ in range(b + 1)] for _ in range(a + 1)]

for i in range(1, n + 1):
    x, y, d = input().split()
    x, y = int(x), int(y)
    robot[i] = [x, y, dic[d]]
    brd[x][y] = i

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

for _ in range(m):
    i, j, k = input().split()
    i, k = int(i), int(k)

    if j == 'F':
        x, y, d = robot[i]
        brd[x][y] = 0

        for _ in range(k):
            x += dx[d]
            y += dy[d]

            if x < 1 or x > a or y < 1 or y > b:
                print(f'Robot {i} crashes into the wall')
                exit(0)
            if brd[x][y] != 0:
                print(f'Robot {i} crashes into robot {brd[x][y]}')
                exit(0)

        robot[i] = [x, y, d]
        brd[x][y] = i

    elif j == 'L':
        robot[i][2] = (robot[i][2] - k) % 4
    elif j == 'R':
        robot[i][2] = (robot[i][2] + k) % 4

print('OK')
