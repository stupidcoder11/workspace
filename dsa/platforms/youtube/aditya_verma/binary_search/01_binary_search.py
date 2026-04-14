'''
Link - https://www.youtube.com/watch?v=QNGL_t_o_QA&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=2

Problem -
Given a sorted array of integers, find if the given target is present
in the array. Return true if it is, otherwise return false.
'''

from typing import List

def bin_search(nums: List[int], target: int) -> bool:
    lb, ub = 0, len(nums) - 1
    while lb <= ub:
        mid = lb + ((ub - lb) >> 1)
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            lb = mid + 1
        else:
            ub = mid - 1
    return False

# Test cases
assert bin_search([1, 2, 3, 4, 5], 3) == True
assert bin_search([1, 2, 3, 4, 5], 6) == False
assert bin_search([], 1) == False
assert bin_search([1], 1) == True
assert bin_search([1, 2], 2) == True