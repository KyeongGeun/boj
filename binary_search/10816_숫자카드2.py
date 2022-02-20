import sys
input = sys.stdin.readline

def left_index(li, v, l=0, r = None):
    if r == None:
        r = len(li)

    while l < r:
        mid = (l + r) // 2
        if li[mid] < v:
            l = mid + 1
        else:
            r = mid

    return l

def right_index(li, v, l=0, r = None):
    if r == None:
        r = len(li)

    while l < r:
        mid = (l + r) // 2
        if v < li[mid]:
            r = mid
        else:
            l = mid + 1

    return l


n = int(input())
li1 = list(map(int, input().split()))

m = int(input())
li2 = list(map(int, input().split()))

li1.sort()

ans = []

for v in li2:
    ans.append(right_index(li1, v) - left_index(li1, v))

print(*ans)