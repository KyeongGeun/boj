import sys
input = sys.stdin.readline

n = int(input())
li = [0] + list(map(int, input().split()))

degree = [0] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True

for i in range(1, n + 1):
    degree[li[i]] += 1

x = 1
y = li[1]

ans = []
while True:
    ans.append(y)
    degree[y] -= 1

    if visited[y]:
        break
    visited[y] = True

    y = li[y]

li2 = []
for i in range(1, n + 1):
    if not visited[i] and degree[i] == 0:
        li2.append(i)

for x in li2:
    if visited[x]:
        continue
    visited[x] = True
    ans.append(x)

    y = li[x]

    while True:
        ans.append(y)

        if visited[y]:
            break
        visited[y] = True

        y = li[y]

li3 = []
for i in range(1, n + 1):
    if not visited[i]:
        li3.append(i)

for x in li3:
    if visited[x]:
        continue
    visited[x] = True
    ans.append(x)

    y = li[x]

    while True:
        ans.append(y)

        if visited[y]:
            break
        visited[y] = True

        y = li[y]

print(len(ans))
print(*ans)
