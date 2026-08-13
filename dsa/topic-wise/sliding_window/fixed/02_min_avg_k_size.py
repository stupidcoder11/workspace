# Problem 2: Minimum Average Subarray I

# Given an integer array nums and an integer k, find the minimum average value of any contiguous subarray of size k.

# Example 1
# Input:
# nums = [1, 12, -5, -6, 50, 3]
# k = 4

# Output:
# 0.5

# Explanation:

# [1,12,-5,-6]  -> average = 0.5
# [12,-5,-6,50] -> average = 12.75
# [-5,-6,50,3]  -> average = 10.5

# Minimum average = 0.5

import math

def solve(nums: list[int], k: int) -> None:
    ans = math.inf
    lb = 0
    csum = 0    # current sum
    for ub in range(len(nums)):
        # expand window
        csum += nums[ub]
        # shrink window maybe conditionally
        while ub - lb + 1 > k:
            csum -= nums[lb]
            lb += 1
        # evaluate when we hit the window size
        if ub - lb + 1 == k:
            ans = min(ans, csum)
    print(ans / k)

solve([1, 12, -5, -6, 50, 3], 4)