import heapq
import sys
input = sys.stdin.readline

def func(num):
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

answer = []

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    S = func(s) # dijkstra

    G = func(g)
    H = func(h)

    x = []
    for _ in range(t):
        x.append(int(input()))

    s = set()

    for v in x:
        if S[g] + G[h] + H[v] == S[v]:
            s.add(v)
        elif S[h] + H[g] + G[v] == S[v]:
            s.add(v)
    
    answer.append( ' '.join( map( str, sorted( list(s) ) ) ) )

print('\n'.join(answer))