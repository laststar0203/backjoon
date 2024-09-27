"""
<예시 입력>
2
500 550 4
450 500 7

<예시 출력>
2050
3200

"""

import sys

N = int(sys.stdin.readline().rstrip())
result = []

for i in range(N):
    A, B, X = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    result.append(A * (X - 1) + B)
    
for i in range(N):
    print(result[i])