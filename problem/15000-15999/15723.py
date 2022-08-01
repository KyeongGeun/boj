# 플로이드 워셜 풀이
import sys
input = sys.stdin.readline

graph = [[float('inf') for _ in range(26)] for _ in range(26)]

for _ in range(int(input())):
    a, _, b = input().split()
    a = ord(a) - 97
    b = ord(b) - 97

    graph[a][b] = 0

for i in range(26):
    for j in range(26):
        for k in range(26):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

ans = []
for _ in range(int(input())):
    a, _, b = input().split()
    a = ord(a) - 97
    b = ord(b) - 97

    if graph[a][b]:
        ans.append('F')
    else:
        ans.append('T')


print(*ans, sep='\n')

# BFS 풀이
# from collections import deque
# import sys
# input = sys.stdin.readline


# def bfs(x, y):
#     visited = [False] * 26
#     dq = deque()
#     dq.append(x)

#     while dq:
#         a = dq.popleft()
#         visited[a] = True

#         for v in alpha[a]:
#             if visited[v]:
#                 continue

#             if v == y:
#                 return True

#             dq.append(v)

#     return False


# alpha = [set() for _ in range(26)]
# parent = [set() for _ in range(26)]

# for _ in range(int(input())):
#     a, _, b = input().split()
#     a = ord(a) - 97
#     b = ord(b) - 97

#     alpha[a].add(b)

# ans = []
# for _ in range(int(input())):
#     a, _, b = input().split()
#     a = ord(a) - 97
#     b = ord(b) - 97

#     if bfs(a, b):
#         ans.append('T')
#     else:
#         ans.append('F')


# print(*ans, sep='\n')
