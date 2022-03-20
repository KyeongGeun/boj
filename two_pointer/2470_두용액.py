import sys
input = sys.stdin.readline
SIZE = 1_000_000_000

n = int(input())
li = list(map(int, input().split()))

li.sort()

i, j = 0, n - 1
mini = 2 * SIZE + 1
answer = (SIZE, SIZE + 1)

while i < j:
    num = li[i] + li[j]
    if num == 0:
        answer = (li[i], li[j])
        break

    if mini > abs(num):
        mini = abs(num)
        answer = (li[i], li[j])

    if num < 0:
        i += 1
    else:
        j -= 1

print(*answer)