import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li.sort()

ans = 0
while li:
    cur = 0
    remove = []

    for i in range(len(li)):
        if cur > li[i]:
            continue

        remove.append(i - cur)
        cur += 1

    for v in remove:
        li.pop(v)

    ans += 1

print(ans)
