import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10_000_000
    except:
        break

    ans = 'danger'
    n = int(input())
    li = [int(input()) for _ in range(n)]
    li.sort()

    l, r = 0, n - 1

    while l < r:
        cur = li[l] + li[r]
        if cur > x:
            r -= 1
        elif cur < x:
            l += 1
        else:
            ans = f'yes {li[l]} {li[r]}'
            break

    print(ans)
