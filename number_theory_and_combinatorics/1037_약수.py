import sys
input = sys.stdin.readline

input()
li = list(map(int, input().split()))

li.sort()

print(li[0]*li[-1])