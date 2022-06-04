import sys
input = sys.stdin.readline

s = input().rstrip()

if s == '100':
    print(0)
    exit(0)

goal = int(s)

n = int(input())
li = list(map(int, input().split()))

if n == 10:
    print(abs(goal - 100))
    exit(0)

if n == 0:
    print(min(abs(goal - 100), len(s)))
    exit(0)

available = [True] * 10
for v in li:
    available[v] = False

for i, v in enumerate(s):
    if not available[int(v)]:
        break
else:
    print(min(abs(goal - 100), len(s)))
    exit(0)

rst1 = int(s)
while rst1 >= 0:
    rst1 -= 1
    for i in range(len(str(rst1))):
        if not available[rst1 % (10 ** (i + 1)) // (10 ** i)]:
            break
    else:
        break
if rst1 == -1:
    rst1 = -5000000


rst2 = int(s)
for _ in range(min(abs(goal - 100), abs(goal - rst1) +
                   len(str(rst1)))):
    rst2 += 1
    for i in range(len(str(rst2))):
        if not available[rst2 % (10 ** (i + 1)) // (10 ** i)]:
            break
    else:
        break

print(min(abs(goal - 100), abs(goal - rst1) +
      len(str(rst1)), abs(goal - rst2) + len(str(rst2))))
