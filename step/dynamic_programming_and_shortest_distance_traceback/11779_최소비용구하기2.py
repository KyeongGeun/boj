import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

a, b = map(int, input().split())
hq = [(a, 0)]
min_w = [float('inf') for _ in range(n + 1)]
pre = [-1 for _ in range(n + 1)]
while hq:
    cur_x, cur_w = heapq.heappop(hq)

    if min_w[cur_x] < cur_w:
        continue

    for new_x, w in graph[cur_x]:
        new_w = cur_w + w

        if min_w[new_x] > new_w:
            min_w[new_x] = new_w
            pre[new_x] = cur_x
            heapq.heappush(hq, (new_x, new_w))

print(min_w[b])

x = b
cnt = 2
answer = [b]

while pre[x] != a:
    cnt += 1
    x = pre[x]
    answer.append(x)

answer.append(a)

print(len(answer))
print(*answer[::-1])