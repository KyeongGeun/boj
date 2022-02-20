# 분할 정복

import sys
input = sys.stdin.readline

def mid_area(x, y, li):
    mid = (x+y)//2
    m = 0
    height = li[mid]
    left, right = mid, mid

    while x < left and right < y:
        if li[left-1] > li[right+1]:
            left -= 1
            height = min(height, li[left])
            m = max(m, height * (right - left + 1) )
        else:
            right += 1
            height = min(height, li[right])
            m = max(m, height * (right - left + 1) )
        
    while x < left:
        left -= 1
        height = min(height, li[left])
        m = max(m, height * (right - left + 1) )

    while right < y:
        right += 1
        height = min(height, li[right])
        m = max(m, height * (right - left + 1) )

    return m

def div(x, y, li):
    mid = (x+y)//2

    if x == y:
        return li[x]

    m = max( div(x, mid, li), div(mid+1, y, li), mid_area(x, y, li) )

    return m

ans = []

while 1:
    n, *li = map(int, input().split())
    if n == 0:
        break

    m = div(0, n-1, li)
    
    ans.append(m)

print(*ans, sep='\n')

# 스택

# from collections import deque
# import sys
# input = sys.stdin.readline

# ans = []

# while 1:
#     n, *li = list(map(int, input().split()))
#     if n == 0:
#         break

#     dq = deque()
#     m = 0

#     for i in range(n):
        
#         while dq and li[dq[-1]] >= li[i]:
#             height = li[dq.pop()]
#             if not dq:
#                 width = i
#             else:
#                 width = i - 1 - dq[-1]
#             print(height * width)
#             m = max(m, height * width)

#         dq.append(i)
    
#     i = n
#     while dq:
#         height = li[dq.pop()]
#         if not dq:
#             width = i
#         else:
#             width = i - 1 - dq[-1]
#         print(height * width)
#         m =  max(m, height * width)

#     ans.append(m)

# print(*ans, sep='\n')