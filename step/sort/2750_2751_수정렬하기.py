import sys
input = sys.stdin.readlinez
arr = []
for _ in range(int(input())):
    arr.append(int(input()))
print(*sorted(arr), sep='\n')