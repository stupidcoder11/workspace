# Last Negative Number in Every Window
# Example
# nums = [-1,2,-3,4,-5]
# k = 3

# Windows:

# [-1,2,-3] -> -3
# [2,-3,4]  -> -3
# [-3,4,-5] -> -5

# Output:

# [-3,-3,-5]

import collections

def solve(nums: list[int], k: int) -> list[int | None]:
    result: list[int | None] = []
    lb = 0
    negatives_dq: collections.deque[int] = collections.deque()  # store indices of negatives for every window
    for ub, num in enumerate(nums):
        # build state
        if num < 0:
            negatives_dq.append(ub)
        # shrink window if needed
        if ub - lb + 1 > k:
            lb += 1
        # remove outdated candidates from deque
        while negatives_dq and negatives_dq[0] < lb:
            negatives_dq.popleft()
        # evaluate
        if ub - lb + 1 == k:
            if negatives_dq:
                result.append(nums[negatives_dq[-1]])
            else:
                result.append(None)
    return result

print(solve([-1,2,-3,4,-5], 3))
print(solve([-1,2,-3,4,-5, 1, 2, 3], 3))