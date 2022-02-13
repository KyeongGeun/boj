import sys

while 1:
    s = sys.stdin.readline().rstrip()
    if s == '.': break
    stack = []
    for v in s:
        if v in '([':
            stack.append(v)
        elif v == ')':
            if not stack or stack.pop() != '(':
                sys.stdout.write('no\n')
                break
        elif v == ']':
            if not stack or stack.pop() != '[':
                sys.stdout.write('no\n')
                break
    else:
        if stack:
            sys.stdout.write('no\n')
        else:
            sys.stdout.write('yes\n')