from collections import deque
import sys
input = sys.stdin.readline


def find(a, b):
    visited = [False] * 10000
    visited[a] = True

    dq = deque()
    dq.append(a)
    cnt = 0
    while dq:
        cnt += 1
        for _ in range(len(dq)):
            x = dq.popleft()

            s = str(x)

            for i in range(4):
                for j in range(10):
                    if i == 0 and j == 0:
                        continue

                    temp = s[:i] + str(j) + s[i + 1:]
                    num = int(temp)

                    if not prime[num]:
                        continue
                    if visited[num]:
                        continue

                    if num == b:
                        return cnt

                    dq.append(num)
                    visited[num] = True

    return 'Impossible'


prime = [False, True] * 5000
prime[1], prime[2] = False, True

for i in range(3, 101, 2):
    if not prime[i]:
        continue
    for j in range(i + i, 10000, i):
        prime[j] = False

ans = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        ans.append(0)
        continue

    ans.append(find(a, b))

print(*ans, sep='\n')
