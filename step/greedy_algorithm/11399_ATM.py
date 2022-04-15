import sys
input = sys.stdin.readline

n = int(input())
*li, = map(int, input().split())
s = 0
li.sort()

for i in range(n):
    s += sum(li[:i+1])

print(s)