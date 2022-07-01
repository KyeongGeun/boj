n, b, w = map(int, input().split())
s = input().rstrip()


def check():
    if cur_b <= b and cur_w >= w:
        return True
    else:
        return False


l, r = 0, 0
cur_b, cur_w = 0, 0
_max = 0

if s[0] == 'B':
    cur_b += 1
else:
    cur_w += 1

if cur_b <= b and cur_w >= w:
    _max = 1

while l <= r and r < n:
    while r < n - 1 and s[r + 1] == 'W':
        r += 1
        cur_w += 1

        if r == n - 1 and check():
            print(max(_max, r - l + 1))
            exit(0)

    if check():
        _max = max(_max, r - l + 1)

        r += 1
        cur_b += 1
    else:
        if l == r or cur_w < w:
            r += 1
            cur_b += 1
            continue

        if s[l] == 'B':
            cur_b -= 1
        else:
            cur_w -= 1

        l += 1

print(_max)
