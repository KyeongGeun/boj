import sys
input = sys.stdin.readline

ans = []
for case in range(1, int(input()) + 1):
    n = int(input())

    li = [list(map(int, input().split())) for _ in range(n)]
    li.sort(key=lambda x: x[0] + x[1])

    leng = 0
    for p, s in li:
        leng = max(leng, p + s + 1)

    dp = [False] * leng
    dp[0] = True
    for p, s in li:
        if s == 0:
            continue
        for i in range(p, -1, -1):
            if dp[i]:
                dp[i + s] = True

    for i in range(leng - 1, -1, -1):
        if dp[i]:
            ans.append(f'Case #{case}: {i}')
            break

print('\n'.join(ans))
