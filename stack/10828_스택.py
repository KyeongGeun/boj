import sys
input = sys.stdin.readline
stack = []

for _ in range(int(input())):
    *li, = input().split()
    if li[0] == 'push':
        stack.append(li[1])
    elif li[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif li[0] == 'size':
        print(len(stack))
    elif li[0] == 'empty':
        print(0 if stack else 1)
    elif li[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)