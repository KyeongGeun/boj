import sys
input = sys.stdin.readline


def dp(x, y=0, z=0):
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if z < 0:
        z = 0

    if memo[x][y][z] != -1:
        return memo[x][y][z]
    if x <= 0 and y <= 0 and z <= 0:
        return 0

    _min = float('inf')
    if x > 0:
        _min = min(_min, dp(x - 9, y - 3, z - 1))
        _min = min(_min, dp(x - 9, y - 1, z - 3))
    if y > 0:
        _min = min(_min, dp(x - 3, y - 9, z - 1))
        _min = min(_min, dp(x - 1, y - 9, z - 3))
    if z > 0:
        _min = min(_min, dp(x - 3, y - 1, z - 9))
        _min = min(_min, dp(x - 1, y - 3, z - 9))

    memo[x][y][z] = _min + 1
    return _min + 1


n = int(input())
hp = list(map(int, input().split()))

if len(hp) == 1:
    memo = [[[-1 for _ in range(1)]
            for _ in range(1)]
            for _ in range(hp[0] + 1)]
    print(dp(hp[0]))
elif len(hp) == 2:
    memo = [[[-1 for _ in range(1)]
            for _ in range(hp[1] + 1)]
            for _ in range(hp[0] + 1)]
    print(dp(hp[0], hp[1]))
elif len(hp) == 3:
    memo = [[[-1 for _ in range(hp[2] + 1)]
            for _ in range(hp[1] + 1)]
            for _ in range(hp[0] + 1)]
    print(dp(hp[0], hp[1], hp[2]))
