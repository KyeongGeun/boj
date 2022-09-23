def recur(s):
    global idx
    temp = ''

    stack = []

    while idx < len(s):
        if s[idx] == '(':
            idx += 1
            temp += recur(s)
        elif s[idx] == ')':
            while stack:
                temp += stack.pop()
            return temp
        elif s[idx] == '*' or s[idx] == '/':
            while stack and stack[-1] != '+' and stack[-1] != '-':
                temp += stack.pop()
            stack.append(s[idx])
        elif s[idx] == '+' or s[idx] == '-':
            while stack:
                temp += stack.pop()
            stack.append(s[idx])
        else:
            temp += s[idx]
        idx += 1

    while stack:
        temp += stack.pop()

    return temp


s = input()

idx = 0

print(recur(s))
