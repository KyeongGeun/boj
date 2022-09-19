from collections import deque
import sys
input = sys.stdin.readline

n, t, g = map(int, input().split())

if n == g:
    print(0)
    exit(0)

visited = [False] * 100000

dq = deque()
dq.append(n)
visited[n] = True

cnt = 0
while cnt < t:
    cnt += 1
    for _ in range(len(dq)):
        x = dq.popleft()

        temp = [x + 1, x * 2]

        if temp[1] < 100000:
            for i in range(4, -1, -1):
                if temp[1] // (10 ** i) != 0:
                    temp[1] -= 10 ** i
                    break

        for v in temp:
            if v > 99999:
                continue
            if visited[v]:
                continue
            visited[v] = True
            if v == g:
                print(cnt)
                exit(0)

            dq.append(v)

print('ANG')
