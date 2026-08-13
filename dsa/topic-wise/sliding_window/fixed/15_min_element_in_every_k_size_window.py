# Q2. Minimum Element in Every Window of Size K
# Example
# nums = [4,2,12,3,5]
# k = 3

# Windows:

# [4,2,12] -> 2
# [2,12,3] -> 2
# [12,3,5] -> 3

# Output:

# [2,2,3]

import collections

def solve(nums: list[int], k: int) -> list[int]:
    lb = 0
    dq: collections.deque[int] = collections.deque()
    ans: list[int] = []
    for ub in range(len(nums)):
        # keep candidate elements only (make monotonic)
        while dq and nums[dq[-1]] > nums[ub]:
            dq.pop()

        dq.append(ub)       # store indices of elements in k-size window

        # shrink window
        if ub - lb + 1 > k:
            lb += 1
        # remove outdated indices
        while dq and dq[0] < lb:
            dq.popleft()
        # evaluate on window hit
        if ub - lb + 1 == k:
            ans.append(nums[dq[0]])
    return ans

print(solve([4,2,12,3,5], 3))