import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

v, e = map(int, input().split())
a = int(input())

graph = {i: [] for i in range(1, v + 1)}

for _ in range(e):
    i, j, w = map(int, input().split())
    graph[i].append((j, w))

dis = {k: float('inf') for k in graph.keys()}

dis[a] = 0
hq = [(dis[a], a)]

while hq:
    cur_dis, cur_x = heapq.heappop(hq)

    if cur_dis > dis[cur_x]:
        continue

    for i, w in graph[cur_x]:
        new_dis = cur_dis + w
        if dis[i] > new_dis:
            dis[i] = new_dis
            heapq.heappush(hq, (new_dis, i))

for i in range(1, v + 1):
    if dis[i] == float('inf'):
        print('INF\n')
        continue
    print(str(dis[i]) + '\n')