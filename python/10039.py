import sys

scores = [int(sys.stdin.readline().rstrip()) for _ in range(5)]
total = 0
for score in scores:
    total += 40 if score < 40 else score
print(int(total / 5)) 