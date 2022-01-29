import sys
input = sys.stdin.readline
print = sys.stdout.write
arr = [0]*10000
for i in range(int(input())):
    arr[int(input())-1] += 1
for i in range(10000):
    for j in range(arr[i]):
        print(str(i+1)+'\n')