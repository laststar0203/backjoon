# 같은 눈 3개
# 같은 눈 2개
# 모드 다른 눈

import sys
nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))

# 야발 모두 if 절로 검사할 순 없잖아!!

count = 0

for i in range(3):
    for j in range(3):
        if i != j and nums[i] == nums[j]:
            count += 1
print(count)