import sys
input = sys.stdin.readline
print = sys.stdout.write

def pre(s):
    print(s)
    if child[s][0] != '.':
        pre(child[s][0])
    if child[s][1] != '.':
        pre(child[s][1])

def in_ord(s):
    if child[s][0] != '.':
        in_ord(child[s][0])
    print(s)
    if child[s][1] != '.':
        in_ord(child[s][1])

def post(s):
    if child[s][0] != '.':
        post(child[s][0])
    if child[s][1] != '.':
        post(child[s][1])
    print(s)

n = int(input())

child = {}

for _ in range(n):
    a, b, c = input().split()
    child[a] = (b, c)

pre('A')
print('\n')
in_ord('A')
print('\n')
post('A')