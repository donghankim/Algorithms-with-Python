# Sequnetial search implemented in python

from typing import List

# boolean return
def seq_search(target: int, nums: List[int]) -> bool:

    for i in range(len(nums)):
        if nums[i] == target:
            return True

    return False

# index return -> -1 returned is target not in list
def seq_search_index(target: int, nums: List[int]) -> int:

    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1

print(seq_search(5, [1,2,3,4,5]))
print(seq_search_index(5, [1,2,3,4,5]))
