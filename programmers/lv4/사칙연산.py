def cal(a, b, o):
    if o == '+':
        return int(a) + int(b)
    else:
        return int(a) - int(b)


def dp(l, r, arr, memo):
    if l == r:
        return (arr[l], arr[l])
    if memo[l][r] != -1:
        return memo[l][r]

    minv = 101000
    maxv = -101000
    for i in range(l + 1, r, 2):
        left = dp(l, i - 1, arr, memo)
        right = dp(i + 1, r, arr, memo)
        for a in range(2):
            for b in range(2):
                v = cal(left[a], right[b], arr[i])
                minv = min(minv, v)
                maxv = max(maxv, v)

    memo[l][r] = (minv, maxv)
    return (minv, maxv)


def solution(arr):
    memo = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]

    return dp(0, len(arr) - 1, arr, memo)[1]
