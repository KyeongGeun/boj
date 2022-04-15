import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

def dijk():
    hq = [(0, 0, 0)]
    dp[0][0] = 0

    while hq:
        cur_d, cur_c, cur_x = heapq.heappop(hq)
        
        if cur_x == n - 1:
            return

        if dp[cur_x][cur_c] < cur_d:
            continue
            
        for new_x, c, d in graph[cur_x]:
            new_d = cur_d + d
            new_c = cur_c + c

            if new_c <= m and dp[new_x][new_c] > new_d:
                for i in range(new_c + 1, m + 1):
                    if dp[new_x][i] > new_d:
                        dp[new_x][i] = new_d
                    else:
                        break
                dp[new_x][new_c] = new_d
                heapq.heappush(hq, (new_d, new_c, new_x))

answer = []
for _ in range(int(input())):
    n, m, k = map(int, input().split())

    graph = [[] for _ in range(n)]
    dp = [[INF for _ in range(m + 1)] for _ in range(n)]

    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u - 1].append((v - 1, c, d))

    dijk()

    mini = min(dp[n - 1])
    if mini == INF:
        answer.append('Poor KCM')
    else:
        answer.append(mini)

print('\n'.join(map(str, answer)))