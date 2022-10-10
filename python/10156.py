import sys

K, N, M = list(map(int, sys.stdin.readline().rstrip().split(' ')))
diff = M - K * N
print(0 if diff >= 0 else -diff)
