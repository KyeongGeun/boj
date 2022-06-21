from collections import deque


f, s, g, u, d = map(int, input().split())

if s == g:
    print(0)
    exit(0)

visited = [False] * (f + 1)
dq = deque()
dq.append(s)

dx = [u, -d]

answer = 'use the stairs'
cnt = 0
while dq:
    for _ in range(len(dq)):
        x = dq.popleft()
        if x == g:
            answer = cnt
            break

        for i in range(2):
            a = x + dx[i]

            if a < 1 or a > f:
                continue

            if visited[a]:
                continue

            visited[a] = True
            dq.append(a)
    cnt += 1

print(answer)
