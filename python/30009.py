"""
<문제>

바나나는 무대 소녀이다. 그녀는 무대의 "포지션 제로"에 서고 싶어 한다. 이 문제에서 무대는 2차원 좌표평면이며, 
"포지션 제로"는 2차원 좌표평면의 원으로 표현된다.

"포지션 제로"의 중심은 (X, Y)이고, 반지름은 R이다.

그러나 바나나가 움직일 수 있는 범위는 제한되어 있다. 
바나나는 N개의 직선 중 하나를 골라, 그 위에서만 움직일 수 있다.

각 직선은 x = Ti(1 <= i <= N)로 표현된다.

바나나가 움직일 수 있는 직선의 개수인 N과 "포지션 제로"의 중심의 좌표와 반지름 X, Y, R, 각 직선의 정보 
Ti가 주어졌을 때, 그녀가 "포지션 제로" 내부에 들어갈 수 있는 직선의 개수 A와 "포지션 제로"의 경계에만 들어갈 수 있는 직선의 개수 B를 출력하라.

<입력>

첫째 줄에 바나나가 움직일 수 있는 직선의 개수 N이 주어진다.

둘째 줄에 세 수 X, Y, R이 공백으로 구분되어 주어진다.

셋째 줄부터 N + 2번째 줄까지는 i + 2(1 <= i <= N)번째 줄에 Ti가 순서대로 주어진다. 입력으로 주어지는 모든 수는 정수이다.

<출력>
바나나가 "포지션 제로" 내부에 들어갈 수 있는 직선의 개수 A와 "포지션 제로"의 경계에만 들어갈 수 있는 직선의 개수 B를 공백으로 구분하여 출력하라.

<입력조건>
- 1 <= N <= 100
- -100 <= X, Y <= 100
- 1 <= R <= 100
- -100 <= Ti <= 100 ( 1 <= i <= N )

<예제입력1>
3
1 2 2
-1
1
5

<예제출력1>
1 1


바나나가 
1번째 직선 위로 움직일 때, "포지션 제로"의 경계에만 들어갈 수 있다. 
2번째 직선 위로 움직일 때, "포지션 제로" 내부에 들어갈 수 있다. 
3번째 직선 위로 움직일 때, "포지션 제로"의 경계에만 들어갈 수도, 내부에 들어갈 수도 없다.

"""

import sys

N = int(sys.stdin.readline().rstrip())
X, Y, R = list(map(int, sys.stdin.readline().rstrip().split(' ')))
Ts = []

a = 0
b = 0

for i in range(N):
    Ti = int(sys.stdin.readline().rstrip())

    if Ti == X - R or Ti == X + R:  # 경계 체크
        a += 1
    elif Ti > X - R and Ti < X + R: # 내부 체크
        b += 1

print(b, a)
    
    
