import sys
input = sys.stdin.readline

li = [int(input()) for _ in range(int(input()))]

minus = []
plus = []
zero = 0

for v in li:
    if v < 0:
        minus.append(v)
    elif v > 0:
        plus.append(v)
    else:
        zero += 1

minus.sort()
plus.sort()

if len(minus) % 2 == 1 and zero > 0:
    minus.pop()

ans = 0
for i in range(1, len(minus), 2):
    ans += minus[i] * minus[i - 1]
for i in range(len(plus) - 2, -1, -2):
    ans += plus[i] * plus[i + 1]
    if plus[i] == 1:
        ans += 1

if len(minus) % 2 == 1:
    ans += minus[-1]
if len(plus) % 2 == 1:
    ans += plus[0]

print(ans)
