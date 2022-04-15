import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 6)

n = int(input()) # 5 <= N <= 1000
w = int(input()) # 1 <= W <= 1000
event = [0]
memo = [[0 for _ in range(w)] for _ in range(w)]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dp(a, b):
    next_w = max(a, b) + 1
    if next_w == w + 1:
        return 0

    if memo[a][b]:
        return memo[a][b]

    x = dp(next_w, b) + dist(event[a] if a != 0 else (1, 1), event[next_w])
    y = dp(a, next_w) + dist(event[b] if b != 0 else (n, n), event[next_w])

    memo[a][b] = min(x, y)

    return memo[a][b]

for _ in range(w):
    x, y = map(int, input().split())
    event.append((x, y))

print(str(dp(0, 0)) + '\n')

a, b = 0, 0
for next_w in range(1, w + 1):
    x = dp(next_w, b) + dist(event[a] if a != 0 else (1, 1), event[next_w])
    y = dp(a, next_w) + dist(event[b] if b != 0 else (n, n), event[next_w])

    if x < y:
        a = next_w
        print('1\n')
    else:
        b = next_w
        print('2\n')