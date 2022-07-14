from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dq = deque([li])
for _ in range(5):
    for _ in range(len(dq)):
        cur_li = dq.popleft()
        # print(*cur_li, sep='\n')
        # print()

        new_li = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            j = 0
            idx = 0
            while j < n:
                if cur_li[i][j] == 0:
                    j += 1
                    continue
                k = j + 1
                while k < n - 1 and cur_li[i][k] == 0:
                    k += 1
                if k < n and cur_li[i][j] == cur_li[i][k]:
                    new_li[i][idx] = cur_li[i][j] + cur_li[i][k]
                    j = k + 1
                else:
                    new_li[i][idx] = cur_li[i][j]
                    j = k
                idx += 1

        dq.append(new_li)

        new_li = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            j = n - 1
            idx = n - 1
            while j > -1:
                if cur_li[i][j] == 0:
                    j -= 1
                    continue
                k = j - 1
                while k > 0 and cur_li[i][k] == 0:
                    k -= 1
                if k > -1 and cur_li[i][j] == cur_li[i][k]:
                    new_li[i][idx] = cur_li[i][j] + cur_li[i][k]
                    j = k - 1
                else:
                    new_li[i][idx] = cur_li[i][j]
                    j = k
                idx -= 1

        dq.append(new_li)

        new_li = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            j = 0
            idx = 0
            while j < n:
                if cur_li[j][i] == 0:
                    j += 1
                    continue
                k = j + 1
                while k < n - 1 and cur_li[k][i] == 0:
                    k += 1
                if k < n and cur_li[j][i] == cur_li[k][i]:
                    new_li[idx][i] = cur_li[j][i] + cur_li[k][i]
                    j = k + 1
                else:
                    new_li[idx][i] = cur_li[j][i]
                    j = k
                idx += 1

        dq.append(new_li)

        new_li = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            j = n - 1
            idx = n - 1
            while j > -1:
                if cur_li[j][i] == 0:
                    j -= 1
                    continue
                k = j - 1
                while k > 0 and cur_li[k][i] == 0:
                    k -= 1
                if k > -1 and cur_li[j][i] == cur_li[k][i]:
                    new_li[idx][i] = cur_li[j][i] + cur_li[k][i]
                    j = k - 1
                else:
                    new_li[idx][i] = cur_li[j][i]
                    j = k
                idx -= 1

        dq.append(new_li)

_max = 0
for li in dq:
    for i in range(n):
        for j in range(n):
            _max = max(_max, li[i][j])

print(_max)
