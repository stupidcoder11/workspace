# Problem: Maximum Sum of Distinct Elements in a Window of Size K

# Given an integer array nums and an integer k, 
# find the maximum sum among all windows of size k that contain only distinct elements.

# If no such window exists, return 0.

# Example 1
# nums = [1,5,4,2,9,9,9]
# k = 3

# Windows:

# [1,5,4] -> distinct -> sum = 10
# [5,4,2] -> distinct -> sum = 11
# [4,2,9] -> distinct -> sum = 15
# [2,9,9] -> not distinct
# [9,9,9] -> not distinct

# Output:

# 15


# Example 2
# nums = [4,4,4]
# k = 3

# Output:

# 0

# import math

# def solve(nums: list[int], k: int) -> None:
#     """
#     Approach
#     ========
#     01 - Loop over all elments till size - k
#     02 - Build window of size k
#     03 - Create distinct elements within that window
#     04 - Calculate sum of distinct elements within that window
#     05 - Track and compute max sum of distinct elements within that window
#     """
#     ans = -math.inf
#     for i in range(len(nums) - k + 1):
#         ans = max(ans, sum(set(nums[i:i+k])))
#     print(ans)


import collections
import math

def solve(nums: list[int], k: int):
    lb = 0
    freq_counter: collections.Counter[int] = collections.Counter()
    rsum = 0
    result = -math.inf
    for ub in range(len(nums)):
        # build the state for current window sum
        rsum += nums[ub]
        # build the state for distinct elements
        freq_counter[nums[ub]] += 1
        # shrink window & update state(s) if needed
        while ub - lb + 1 > k:
            # update the state for current sum
            rsum -= nums[lb]
            # update the state for distinct elements
            freq_counter[nums[lb]] -= 1
            if freq_counter[nums[lb]] == 0:
                del freq_counter[nums[lb]]
            lb += 1
        # evaluate the ans when window size is hit
        if ub - lb + 1 == k:
            if len(freq_counter) == k:
                result = max(result, rsum)

    if math.isinf(result):
        print(0)
    else:
        print(result)
            

solve([1,5,4,2,9,9,9], 3)
solve([4, 4, 4], 3)