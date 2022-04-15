import sys
input = sys.stdin.readline

n, s = map(int, input().split())
li = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    li[i] = li[i - 1] + li[i]

mini = float('inf')
i, j = 0, 1
while i < j and j < n + 1:
    num = li[j] - li[i]
    if num < s:
        j += 1
    elif num >= s:
        mini = min(mini, j - i)
        i += 1

if mini == float('inf'):
    print(0)
else:
    print(mini)