# Problem 1: Maximum Sum Subarray of Size K

# Given an array of integers and an integer k, find the maximum sum of any contiguous subarray of size k.

# Example 1
# Input:
# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# Output:
# 9

# Explanation:

# [2,1,5] -> 8
# [1,5,1] -> 7
# [5,1,3] -> 9
# [1,3,2] -> 6

# Maximum = 9

import math

def solve(nums: list[int], k: int) -> None:
    ans = -math.inf
    lb = 0
    csum = 0
    for ub in range(len(nums)):
        # expand window
        csum += nums[ub]
        # shrink the window maybe, if it's more than size
        while ub - lb + 1 > k:
            csum -= nums[lb]
            lb += 1
        # evaluate maybe if window size is reached
        if ub - lb + 1 == k:
            ans = max(ans, csum)
    print(ans)


solve([2, 1, 5, 1, 3, 2], 3)