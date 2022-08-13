import sys
input = sys.stdin.readline

n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

li.sort(key=lambda x: -x[1])

time = li[0][1]

for a, b in li:
    time = min(time, b) - a

    if time < 0:
        print(-1)
        exit(0)

print(time)
