import sys
T = int(sys.stdin.readline().rstrip())


for _ in range(T):

    a, b =  list(map(int, sys.stdin.readline().rstrip().split(' ')))
    m = a * b

    # get gcd
    if(a < b):
        tmp = b
        b = a
        a = tmp

    while b != 0:
        r = a % b 
        a = b
        b = r


    # get lcm
    print(int(m / a))

