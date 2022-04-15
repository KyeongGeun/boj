import sys
input = sys.stdin.readline
li = []

for _ in range(int(input())):
    n = int(input())
    if n != 0:
        li.append(n)
    else:
        li.pop()

print(sum(li))