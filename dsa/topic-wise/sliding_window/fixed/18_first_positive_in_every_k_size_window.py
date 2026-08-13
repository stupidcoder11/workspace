# First Positive Number in Every Window
# Example
# nums = [-1,-2,5,-3,4]
# k = 3

# Windows:

# [-1,-2,5] -> 5
# [-2,5,-3] -> 5
# [5,-3,4]  -> 5

# Output:

# [5,5,5]

import collections

def solve(nums: list[int], k: int) -> list[int | None]:
    result: list[int | None] = []
    lb = 0
    positives_dq: collections.deque[int] = collections.deque()  # store indices of positives in window
    for ub, num in enumerate(nums):
        # build state during expansion
        if num > 0:
            positives_dq.append(ub)
        # shrink window
        if ub - lb + 1 > k:
            lb += 1
        # remove outdated candidates
        while positives_dq and positives_dq[0] < lb:
            positives_dq.popleft()
        # evaluate
        if ub - lb + 1 == k:
            if positives_dq:
                result.append(nums[positives_dq[0]])
            else:
                result.append(None)

    return result

print(solve([-1,-2,5,-3,4], 3))
print(solve([-1,-2,-5,3,-5, -7, -8], 3))