from collections import deque

n, k = map(int, input().split())
li = [0] * 100001
def bfs(v):
    q = deque([v])

    d = [-1, 1, 0]

    while q:
        x = q.popleft()
        d[2] = x
        
        for i in range(3):
            a = x + d[i]

            if 0 <= a <= 100000:
                if li[a] == 0 or li[a] > li[x] + 1:
                    li[a] = li[x] + 1
                    if a == k:
                        break
                    q.append(a)

bfs(n)
li[n] = 0
print(li[k])