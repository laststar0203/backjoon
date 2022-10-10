import sys
nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))

n = 0
max = 0
count = 0

for i in range(len(nums)):

    n = nums[i]

    if max < nums[i]:
        max = nums[i]

    for j in range(len(nums)):
        if i == j:
            continue
        if nums[i] == nums[j]:
            count += 1
    
    if count != 0:
        count += 1
        break

if count == 3:
    print(10000 + n * 1000)
elif count == 2:
    print(1000 + n * 100)
else:
    print(max * 100)