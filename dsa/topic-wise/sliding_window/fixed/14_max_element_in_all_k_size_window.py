# Q1. Maximum Element in Every Window of Size K
# Example
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3

# Windows:

# [1,3,-1]    -> 3
# [3,-1,-3]   -> 3
# [-1,-3,5]   -> 5
# [-3,5,3]    -> 5
# [5,3,6]     -> 6
# [3,6,7]     -> 7

# Output:

# [3,3,5,5,6,7]

import collections

def solve(nums: list[int], k: int) -> list[int]:
    lb = 0
    dq: collections.deque[int] = collections.deque()
    result: list[int] = []

    for ub in range(len(nums)):

        # Remove dominated candidates
        while dq and nums[dq[-1]] < nums[ub]:
            dq.pop()

        # Add current index
        dq.append(ub)

        # Shrink window if needed
        if ub - lb + 1 > k:
            lb += 1

        # Remove expired indices
        while dq and dq[0] < lb:
            dq.popleft()

        # Evaluate
        if ub - lb + 1 == k:
            result.append(nums[dq[0]])

    return result

print(solve([1,3,-1,-3,5,3,6,7], 3))
