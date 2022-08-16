import sys
input = sys.stdin.readline

s = input().rstrip()

stack = []
for c in s:
    stack.append(c)

    if len(stack) < 4:
        continue

    if stack[-2] == 'A' and stack[-1] == stack[-3] == stack[-4] == 'P':
        stack.pop()
        stack.pop()
        stack.pop()

if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')
