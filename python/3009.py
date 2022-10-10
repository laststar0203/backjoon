import sys

pos = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(3)]

x_pos = sorted([p[0] for p in pos])
y_pos = sorted([p[1] for p in pos])


print(
    x_pos[0] if x_pos[0] != x_pos[1] else x_pos[2],
    y_pos[0] if y_pos[0] != y_pos[1] else y_pos[2],
)