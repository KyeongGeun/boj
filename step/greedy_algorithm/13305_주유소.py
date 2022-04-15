import sys
input = sys.stdin.readline

n = int(input())
leng = list(map(int, input().split()))
cost = list(map(int, input().split()))

s = leng[0]*cost[0]
mi = cost[0]

for i in range(1, n-1):
    mi = min(mi, cost[i])
    s += mi*leng[i]

print(s)