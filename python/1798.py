import sys
S = int(sys.stdin.readline().rstrip())
count = 0

for i in range(1, 4294967295):
    
    if S >= i:
        count += 1
    else:
        break
    S -= i

print(count)