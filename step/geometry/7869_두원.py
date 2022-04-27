import math
import sys
input = sys.stdin.readline

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

if d >= r1 + r2:
    print('0.000')
    exit(0)

if d <= abs(r1 - r2):
    print(f'{min(r1 ** 2, r2 ** 2) * math.pi:.3f}')
    exit(0)

# 코사인 제2 법칙
# a ** 2 = b ** 2 + c ** 2 - 2 * b * c * cos(A)
# => cos(A) = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
theta1 = 2 * math.acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
theta2 = 2 * math.acos((r2 ** 2 + d ** 2 - r1 ** 2) / (2 * r2 * d))

s1 = .5 * theta1 * (r1 ** 2)
s2 = .5 * theta2 * (r2 ** 2)
s3 = d * r1 * math.sin(theta1 / 2)

print(f'{s1 + s2 - s3:.3f}')
