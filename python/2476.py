import sys

T = int(sys.stdin.readline().rstrip())
max = 0

for _ in range(T):
    nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    n = 0
    n_max = 0
    count = 0

    for i in range(len(nums)):

        n = nums[i]

        if n_max < nums[i]:
            n_max = nums[i]

        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] == nums[j]:
                count += 1
        
        if count != 0:
            count += 1
            break
        
    if count == 3:
        value = 10000 + n * 1000
    elif count == 2:
        value = 1000 + n * 100
    else:
        value = n_max * 100

    if max < value:
        max = value

print(max)