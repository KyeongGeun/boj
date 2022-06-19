import sys
input = sys.stdin.readline

n, k = map(int, input().split())
st = input().rstrip()

stack = [st[0]]

answer = ''
for i in range(1, len(st)):
    while stack and st[i] > stack[-1]:
        stack.pop()
        k -= 1

        if k == 0:
            answer = ''.join(stack) + st[i:]
            break
    else:
        stack.append(st[i])
        continue
    break
else:
    for i in range(k):
        stack.pop()
    answer = ''.join(stack)

print(answer)
