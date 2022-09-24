import sys
input = sys.stdin.readline

billion = 1_000_000_000

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


mmax = max(a)
idx1 = a.index(mmax)
idx2 = n - a[::-1].index(mmax) - 1

ans = (sum(a) + mmax * (m - 1)) * billion + sum(b) + b[0] * idx1
if idx1 != idx2:
    ans += (idx2 - idx1) * max(b) + b[-1] * (n - idx2 - 1)
else:
    ans += b[-1] * (n - idx1 - 1)

print(ans)
