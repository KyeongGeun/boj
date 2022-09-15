import sys
input = sys.stdin.readline

input()
li = sorted(list(map(int, input().split())))

max = 0
for v in li:
    if v > max + 1:
        break
    else:
        max += v

print(max + 1)
