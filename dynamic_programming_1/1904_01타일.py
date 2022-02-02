import sys
input = sys.stdin.readline

n = int(input())

pre = 0
result = 1
for i in range(1, n+1):
    result, pre = (result+pre)%15746, result

print(result)