# binary search implemented in python

import random
from typing import List

def binary_search(target: int, nums: List[int]) -> int:

    print(nums, "tagret:", target)
    start_index = 0
    end_index = len(nums) -1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if nums[mid_index] == target:
            return True

        elif target < nums[mid_index]:
            end_index = mid_index - 1

        else:
            start_index = mid_index + 1

    return False

nums = []

for i in range(10):
    nums.append(random.randint(0,100))

nums.sort()
print(binary_search(5, nums))
print(binary_search(5, nums))
