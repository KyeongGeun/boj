import sys
input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]

stack = []
cnt = 0
s = ''

for i in range(1, n+1):
    while stack and stack[-1] == seq[cnt]:
        s += '-\n'
        stack.pop()
        cnt += 1
    s += '+\n'
    stack.append(i)

while stack and stack[-1] == seq[cnt]:
        s += '-\n'
        stack.pop()
        cnt += 1

if stack:
    print('NO')
else:
    print(s, end='')