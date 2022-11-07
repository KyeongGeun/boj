def solution(s):
    stack = []

    for c in s:
        if c == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        else:
            stack.append(c)

    return not stack
