import sys
input = sys.stdin.readline

def func(num):
    min_d = [float('inf')] * (v + 1)
    min_d[num] = 0

    for i in range(v):
        for j in range(e):
            a, b, c = graph[j]
            d = min_d[a] + c
            if min_d[a] != float('inf') and min_d[b] > d:
                min_d[b] = d
                if i == v - 1:
                    return [-1]
    
    return min_d
        
v, e = map(int, input().split())

graph = []

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

min_d = func(1)

if min_d[0] == -1:
    print(-1)
else:
    answer = []
    for i in range(2, v + 1):
        if min_d[i] == float('inf'):
            answer.append('-1')
        else:
            answer.append(str(min_d[i]))

    print('\n'.join(answer))