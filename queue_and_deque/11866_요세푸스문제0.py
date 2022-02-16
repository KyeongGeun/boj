from collections import deque

n, k = map(int, input().split())
ans = []
q = deque([str(i) for i in range(1, n+1)])

for _ in range(n):
    q.rotate(-k+1)
    ans.append(q.popleft())

print('<'+', '.join(ans)+'>')