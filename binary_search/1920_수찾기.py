import sys
input = sys.stdin.readline

def bs(li, v):
    l = 0
    r = len(li) - 1
    mid = (l + r) // 2
    while l < r:
        if v < li[mid]:
            r = mid - 1
            mid = (l + r) // 2
        elif v > li[mid]:
            l = mid + 1
            mid = (l + r) // 2
        else:
            return 1
    
    if li[l] == v:
        return 1
    else:
        return 0

n = int(input())
li1 = list(map(int, input().split()))

m = int(input())
li2 = list(map(int, input().split()))

li1.sort()

ans = []

for v in li2:
    ans.append(bs(li1, v))

print(*ans, sep='\n')