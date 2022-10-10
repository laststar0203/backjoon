import sys
T = int(sys.stdin.readline().rstrip())


for _ in range(T):
    inputs = sys.stdin.readline().rstrip().split(' ')
    num = float(inputs[0])
    for i in range(len(inputs)):
        if inputs[i] == '@':
            num *= 3
        elif inputs[i] == '%':
            num += 5
        elif inputs[i] == '#':
            num -= 7
    print('{:.2f}'.format(num))