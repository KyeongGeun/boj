import sys
input = sys.stdin.readline
n = int(input())
result = []
*li, = map(int, input().split())
*oper, = map(int, input().split()) # +, -, *, /
def func(N,a):
    global result
    if N == n-1:
        result.append(a)
        return
    for i in range(4):
        if oper[i] != 0:
            oper[i] -= 1
            if i == 0:
                func(N+1, a + li[N+1])
            elif i == 1:
                func(N+1, a - li[N+1])
            elif i == 2:
                func(N+1, a * li[N+1])
            else:
                func(N+1, int(a / li[N+1]))
            oper[i] += 1
func(0, li[0])
print(max(result))
print(min(result))