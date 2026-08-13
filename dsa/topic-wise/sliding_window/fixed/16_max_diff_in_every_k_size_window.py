# Maximum Difference in Every Window

# Return:

# max(window) - min(window)

# for every window.

# Example
# nums = [4,2,12,3]
# k = 3

# Windows:

# [4,2,12] -> 12 - 2 = 10
# [2,12,3] -> 12 - 2 = 10

# Output:

# [10,10]

import collections

def solve(nums: list[int], k: int) -> list[int]:
    mono_inc_dq: collections.deque[int] = collections.deque()
    mono_dec_dq: collections.deque[int] = collections.deque()
    lb = 0
    result: list[int] = []

    for ub, num in enumerate(nums):
        # prepare monotonic decreasing deque
        while mono_dec_dq and nums[mono_dec_dq[-1]] < num:
            mono_dec_dq.pop()

        mono_dec_dq.append(ub)

        # prepare monotonic decreasing deque
        while mono_inc_dq and nums[mono_inc_dq[-1]] > num:
            mono_inc_dq.pop()
        
        mono_inc_dq.append(ub)

        # shrink window (& update state if needed)
        while ub - lb + 1 > k:
            lb += 1
        
        # remove outdated elements from window
        while mono_dec_dq and mono_dec_dq[0] < lb:
            mono_dec_dq.popleft()

        # evaluate
        if ub - lb + 1 == k:
            result.append(nums[mono_dec_dq[0]] - nums[mono_inc_dq[0]])

    return result

print(solve([4,2,12,3], 3))