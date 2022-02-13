import sys, math
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

for i in range(1, n):
    g = math.gcd(li[0], li[i])
    print(f'{li[0]//g}/{li[i]//g}')