# 신발끈 공식
# https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D
import sys
input = sys.stdin.readline

n = int(input())

li = [0] * n


for i in range(n):
    a, b = map(int, input().split())
    li[i] = (a, b)

# x_n * y_1 - x_1 * y_n
ans = li[n - 1][0] * li[0][1] - li[0][0] * li[n - 1][1]

for i in range(n - 1):
    # x_i * y_i+1
    ans += li[i][0] * li[i + 1][1]
    # x_i+1 * y_i
    ans -= li[i + 1][0] * li[i][1]

ans = abs(ans) * .5

print(f'{ans:.1f}')
