# Maximum Sum Window Having Exactly K Distinct Elements

# Given an integer array nums, an integer window_size, and an integer k.

# Find the maximum sum among all contiguous windows of size window_size that contain exactly k distinct elements.

# If no such window exists, return 0.

# Example 1
# nums = [1, 2, 1, 2, 3]
# window_size = 4
# k = 2

# Windows:

# [1,2,1,2]

# Distinct elements:

# {1,2}

# Count:

# 2

# Sum:

# 6

# Valid.

# [2,1,2,3]

# Distinct elements:

# {1,2,3}

# Count:

# 3

# Invalid.

# Answer:

# 6
# Example 2
# nums = [4,4,4,5,5]
# window_size = 3
# k = 1

# Windows:

# [4,4,4]

# Distinct count:

# 1

# Sum:

# 12

# Valid.

# [4,4,5]

# Distinct count:

# 2

# Invalid.

# [4,5,5]

# Distinct count:

# 2

# Invalid.

# Answer:

# 12
# Example 3
# nums = [1,2,3,4]
# window_size = 2
# k = 3

# No window of size 2 can have 3 distinct elements.

# Answer:

# 0
# Constraints
# 1 <= len(nums) <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= window_size <= len(nums)
# 1 <= k <= window_size
# Expected Complexity
# Time:  O(n)
# Space: O(window_size)

import collections

def solve(nums: list[int], window_size: int, k: int) -> None:
    lb = 0
    freq_counter: collections.Counter[int] = collections.Counter()
    rsum = 0
    result = 0
    
    for ub in range(len(nums)):
        # expanding window and updating state
        rsum += nums[ub]
        freq_counter[nums[ub]] += 1
        # shrink window and update state if needed
        if ub - lb + 1 > window_size:
            rsum -= nums[lb]
            freq_counter[nums[lb]] -= 1
            if freq_counter[nums[lb]] == 0:
                del freq_counter[nums[lb]]
            lb += 1
        # evaluate when window is hit
        if ub - lb + 1 == window_size:
            # check if it's a valid candidate
            if len(freq_counter) == k:
                result = max(result, rsum)
    print(result)

solve([1, 2, 1, 2, 3], 4, 2)
solve([4,4,4,5,5], 3, 1)
solve([1,2,3,4], 2, 3)