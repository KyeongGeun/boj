from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
d = deque([i for i in range(1, n+1)])

cnt = 0
ans = 0

for v in li:
    if d[0] == v:
        d.popleft()
        n -= 1
    else:
        while d[0] != v:
            d.rotate(-1)
            cnt += 1
        d.popleft()
        if cnt < n/2:
            ans += cnt
        else:
            ans += n - cnt
        n -= 1
        cnt = 0

print(ans)
