n = int(input())
k = int(input())

l, r = 1, k

while l <= r:
    mid = (l + r) // 2
    
    cnt = 0

    for i in range(1, n + 1):
        q = mid // i
        cnt += q if q <= n else n

    if cnt < k:
        l = mid + 1
    else:
        r = mid - 1
    
print(l) # l == r+1로 끝나기 때문