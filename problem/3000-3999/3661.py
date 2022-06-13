import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p, n = map(int, input().split())
    li = list(map(int, input().split()))

    pair = [[li[i], i] for i in range(n)]
    pair.sort(key=lambda x: x[0])

    start = 0
    num = n
    for i in range(n):
        if pair[i][0] < p / num:
            p -= pair[i][0]
            num -= 1
        else:
            start = i
            break

    if num == 0:
        print('IMPOSSIBLE')
        continue

    pair2 = sorted(pair[start:], key=lambda x: (-x[0], x[1]))

    for i in range(n - start):
        if p % num == 0:
            pair2[i][0] = p // num
        else:
            pair2[i][0] = p // num + 1
            p -= pair2[i][0]
            num -= 1

    pair = pair[:start] + pair2
    pair.sort(key=lambda x: x[1])

    ans = [pair[i][0] for i in range(n)]
    print(*ans)
