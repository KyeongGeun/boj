import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda a: (a[1], a[0]))
print(*[f'{x[0]} {x[1]}' for x in arr], sep='\n')