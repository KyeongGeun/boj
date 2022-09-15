import sys
input = sys.stdin.readline

input()
li = sorted(list(map(int, input().split())))

max = 1
for v in li:
    if v > max:
        break
    else:
        max += v

print(max)
