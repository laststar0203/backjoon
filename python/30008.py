"""
<예제 입력1>
255 5
30 37 50 7 35

<예제 출력1>
2 3 3 1 3

<예제 입력2>
255 5
1 1 1 1 1

<예제 출력2>
1 1 1 1 1

<예제 입력3>
100 9
4 11 23 40 60 77 89 96 100

<예제 출력3>
1 2 3 4 5 6 7 8 9

"""

import sys

N, K = list(map(int, sys.stdin.readline().rstrip().split(' ')))
G = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for g in G:
    t = int(g * 100 / N)
    if t >= 0 and t <= 4:
        grade = 1
    elif t > 4 and t <= 11:
        grade = 2
    elif t > 11 and t <= 23:
        grade = 3
    elif t > 23 and t <= 40:
        grade = 4
    elif t > 40 and t <= 60:
        grade = 5
    elif t > 60 and t <= 77:
        grade = 6
    elif t > 44 and t <= 89:
        grade = 7
    elif t > 89 and t <= 96:
        grade = 8
    elif t > 96 and t <= 100:
        grade = 9
    
    print(grade, end=" ")
    
    