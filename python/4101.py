import sys

while True:
    A, B = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    if A == B == 0:
        break

    if A > B:
        print('Yes')
    else:
        print('No')