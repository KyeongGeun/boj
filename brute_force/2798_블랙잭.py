import sys
input = sys.stdin.readline
n, m = map(int, input().split())
*arr, = sorted(map(int, input().split()[::-1]))
max = 0 
for i in range(n-2):
    if arr[i]*3 >= m:
        break
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = arr[i]+arr[j]+arr[k]
            if max < sum <= m:
                max = sum
print(max)