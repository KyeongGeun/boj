import sys
input = sys.stdin.readline
arr = []
for i in range(int(input())):
    arr.append(list(map(int, input().split())))
for i in range(len(arr)):
    cnt = 1
    for j in range(len(arr)):
        if i == j: continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    print(cnt)