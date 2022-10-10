# 파이썬이면 그냥 풀리는 문제이긴 하지만 나는 그딴 저급한 방법으론 하지 않겠어!
import sys

A = list(sys.stdin.readline().rstrip())
operator = sys.stdin.readline().rstrip()
B = list(sys.stdin.readline().rstrip())

a_power = len(A) - 1
b_power = len(B) - 1

if operator == '*':
    print('1' + '0' * (a_power + b_power))
elif operator == '+':
    if a_power == b_power:
        A[0] = '2'
        print(''.join(A))
    elif a_power > b_power:
        A[-b_power - 1] = '1'
        print(''.join(A))
    else:
        B[-a_power - 1] = '1'
        print(''.join(B))
        
    