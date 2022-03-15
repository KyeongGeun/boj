import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

a, b = map(int, input().split())

def dijkstra(num):
    min_d = [sys.maxsize] * (n + 1)
    min_d[num] = 0
    hq = [(0, num)]
    
    while hq:
        cur_d, cur_x = heapq.heappop(hq)

        if cur_d > min_d[cur_x]:
            continue
    
        for new_x, d in graph[cur_x]:
            new_d = cur_d + d
            if min_d[new_x] > new_d:
                min_d[new_x] = new_d
                heapq.heappush(hq, (new_d, new_x))

    return min_d

one = dijkstra(1)
A = dijkstra(a)
B = dijkstra(b)

result = min( one[a] + B[n], one[b] + A[n] ) + A[b]
if result > 200000000:
    print(-1)
else:
    print(result)