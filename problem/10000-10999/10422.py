import sys
input = sys.stdin.readline

ans = []
facto = [1] * (5001)

for i in range(2, 5001):
    facto[i] = facto[i - 1] * i

for _ in range(int(input())):
    n = int(input())

    if n < 2:
        ans.append(0)
        continue

    if n % 2 == 1:
        ans.append(0)
        continue

    n //= 2

    catalan = facto[2 * n] // (facto[n + 1] * facto[n])
    catalan %= 1_000_000_007

    ans.append(catalan)

print(*ans, sep='\n')
