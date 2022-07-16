from collections import deque
import sys
input = sys.stdin.readline


def geton(cur, opp):
    global curtime

    # cur에 사람이 더 이상 안올 때
    if not cur:

        # opp에도 아직 사람이 없을 때
        if curtime < opp[0][0]:
            curtime = opp[0][0]
        return

    # cur에 사람이 아직 안왔을 때
    if cur[0][0] > curtime:

        # cur보다 opp에 사람이 빨리올 때
        if opp and cur[0][0] > opp[0][0]:

            # opp에도 아직 사람이 없을 때
            if curtime < opp[0][0]:
                curtime = opp[0][0]
            return

        # opp보다 cur에 사람이 빨리올 때
        else:
            curtime = cur[0][0]

    while len(riding) < m and cur and cur[0][0] <= curtime:
        riding.append(cur.popleft()[1])


m, t, n = map(int, input().split())

left = deque()
right = deque()

for i in range(n):
    a, b = input().split()
    a = int(a)

    if b == 'left':
        left.append((a, i))
    else:
        right.append((a, i))

location = 0
curtime = 0

riding = []
ans = [0] * n
while left or right:
    if location == 0:
        geton(left, right)
    else:
        geton(right, left)

    curtime += t
    while riding:
        ans[riding.pop()] = curtime

    location = (location + 1) % 2

print(*ans, sep='\n')
