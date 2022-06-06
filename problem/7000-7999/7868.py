import sys
input = sys.stdin.readline

p1, p2, p3, i = map(int, input().split())
_max = 10 ** 18

seq = []

for x in range(0, i + 1):
    if p1 ** x > _max:
        break
    for y in range(0, i + 1):
        if p1 ** x * p2 ** y > _max:
            break
        for z in range(0, i + 1):
            v = p1 ** x * p2 ** y * p3 ** z
            if v > _max:
                break

            seq.append(v)

seq.sort()

print(seq[i])
