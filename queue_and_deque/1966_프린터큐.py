from collections import deque
import sys
input = sys.stdin.readline

q = deque()
cnt = 1
ans = []

for _ in range(int(input())):
    n, k = map(int, input().split())
    for v in map(int, input().split()):
        q.append(v)
    for _ in range(n):
        m = max(q)
        while q[0] != m:
            q.rotate(-1)
            k -= 1
            k %= n
        if k == 0:
            ans.append(cnt)
            break
        else:
            q.popleft()
            cnt += 1
            k -= 1
            n -= 1
    q.clear()
    cnt = 1

print('\n'.join(map(str, ans)))