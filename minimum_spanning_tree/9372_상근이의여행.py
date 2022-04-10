import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    n, m = map(int, input().split())

    for _ in range(m):
        _, _ = map(int, input().split())

    answer.append(str(n - 1))

print('\n'.join(answer))
