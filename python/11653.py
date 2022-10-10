import sys
N = int(sys.stdin.readline().rstrip())

for i in range(2, N + 1):

    while N != 1 and N % i == 0:
        print(i)
        N /= i





