import sys
input = sys.stdin.readline

li = [1, 1, 1, 2, 2]
for i in range(5, 100):
    li.append(li[i-1] + li[i-5])

for _ in range(int(input())):
    n = int(input())
    print(li[n-1])