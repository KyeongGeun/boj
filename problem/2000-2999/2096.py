import sys
input = sys.stdin.readline

maxPrev = [0, 0, 0]
maxCur = [0, 0, 0]

minPrev = [0, 0, 0]
minCur = [0, 0, 0]

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    maxCur[0] = max(maxPrev[0] + a, maxPrev[1] + a)
    maxCur[1] = max(maxPrev[0] + b, maxPrev[1] + b, maxPrev[2] + b)
    maxCur[2] = max(maxPrev[1] + c, maxPrev[2] + c)

    maxPrev = maxCur[:]

    minCur[0] = min(minPrev[0] + a, minPrev[1] + a)
    minCur[1] = min(minPrev[0] + b, minPrev[1] + b, minPrev[2] + b)
    minCur[2] = min(minPrev[1] + c, minPrev[2] + c)

    minPrev = minCur[:]


print(max(maxCur), min(minCur))
