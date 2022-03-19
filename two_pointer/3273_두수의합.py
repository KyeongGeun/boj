import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
x = int(input())

li.sort()

i = 0
j = n - 1
cnt = 0

while i < j:
    k = li[i] + li[j]
    if k == x:
        cnt += 1
        i += 1
    elif k > x:
        j -= 1
    elif k < x:
        i += 1

print(cnt)