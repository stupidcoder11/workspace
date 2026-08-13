# First Even Number in Every Window
# Example
# nums = [1,3,4,5,6]
# k = 3

# Windows:

# [1,3,4] -> 4
# [3,4,5] -> 4
# [4,5,6] -> 4

# Output:

# [4,4,4]

from collections import deque

def solve(nums: list[int], k: int) -> list[int | None]:
    result: list[int | None] = []
    lb = 0
    dq: deque[int] = deque()    # to store indices of even numbers in window
    for ub, num in enumerate(nums):
        # build state (conditionally)
        if not (num&1):
            dq.append(ub)
        # shrink window (& udpate state if needed)
        if ub - lb + 1 > k:
            lb += 1
        # remove outdated candidates from deque
        while dq and dq[0] < lb:
            dq.popleft()
        print(f'num = {num}, dq = {[nums[i] for i in dq]}')
        # evaluate
        if ub - lb + 1 == k:
            if dq:
                result.append(nums[dq[0]])
            else:
                result.append(None)

    return result

print(solve([1,3,4,5,6,7,9,11], 3))