n = int(input())
li = list(map(int, input().split()))

lis = [li[0]]

def bs_left(li, v, l=0, r=None):
    if r == None:
        r = len(li) - 1

    while l <= r:
        mid = (l + r) // 2

        if li[mid] < v:
            l = mid + 1
        else:
            r = mid - 1

    return l

for i in range(1, n):
    if lis[-1] < li[i]:
        lis.append(li[i])
    else:
        idx = bs_left(lis, li[i])
        if lis[idx] > li[i]:
            lis[idx] = li[i]

print(len(lis))