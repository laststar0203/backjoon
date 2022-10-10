import sys
print(sorted(list(map(int, sys.stdin.readline().rstrip().split(' '))), reverse=True)[1])