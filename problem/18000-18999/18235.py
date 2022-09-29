from collections import deque
from math import log2


n, a, b = map(int, input().split())

memo = [False] * (n + 1)
memo[a] = True

five = deque([a])
six = deque([b])

dx = [1, -1]
for day in range(1, int(log2(n)) + 1):

    for _ in range(len(five)):
        v = five.popleft()

        memo[v] = False

        for i in range(2):
            nx = v + dx[i]

            if nx < 1 or nx > n:
                continue

            memo[nx] = True
            five.append(nx)

    for _ in range(len(six)):
        v = six.popleft()

        for i in range(2):
            nx = v + dx[i]

            if nx < 1 or nx > n:
                continue

            if memo[nx] == True:
                print(day)
                exit(0)

            six.append(nx)

    dx[0] <<= 1
    dx[1] <<= 1

print(-1)
