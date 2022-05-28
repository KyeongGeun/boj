# 세그먼트 트리 풀이 4852ms

import sys
input = sys.stdin.readline


def calcu(x, i, j, a, b):
    if i > b or j < a:
        return 0
    if a <= i and j <= b:
        return tree[x]

    mid = (i + j) // 2
    l = calcu(x * 2 + 1, i, mid, a, b)
    r = calcu(x * 2 + 2, mid + 1, j, a, b)

    return l + r


def update(x, i, j, idx):
    if idx < i or j < idx:
        return
    if i == j:
        tree[x] = 1
        return

    mid = (i + j) // 2
    update(x * 2 + 1, i, mid, idx)
    update(x * 2 + 2, mid + 1, j, idx)

    tree[x] = tree[x * 2 + 1] + tree[x * 2 + 2]


n = int(input())
li = list(map(int, input().split()))
li = [(li[i], i) for i in range(n)]
li.sort()
tree = [0] * (n * 4)

cnt = 0
for _, i in li:
    cnt += calcu(0, 0, n - 1, i, n - 1)
    update(0, 0, n - 1, i)

print(cnt)


# 병합 정렬 풀이 576ms

# import sys
# input = sys.stdin.readline


# def merge(i, j):
#     if i == j:
#         return [li[i]]

#     global cnt

#     mid = (i + j) // 2
#     left = merge(i, mid)
#     right = merge(mid + 1, j)

#     ssum = []
#     idx1, idx2 = 0, 0
#     while idx1 < len(left) and idx2 < len(right):
#         if left[idx1] > right[idx2]:
#             ssum.append(right[idx2])
#             cnt += len(left) - idx1
#             idx2 += 1
#         else:
#             ssum.append(left[idx1])
#             idx1 += 1

#     while idx1 < len(left):
#         ssum.append(left[idx1])
#         idx1 += 1

#     while idx2 < len(right):
#         ssum.append(right[idx2])
#         idx2 += 1

#     return ssum


# n = int(input())
# li = list(map(int, input().split()))
# cnt = 0

# merge(0, n - 1)
# print(cnt)
