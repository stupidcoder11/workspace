# Count Windows Where Maximum Element Is Even
# nums = [1,4,2,3,6]
# window_size = 3

# Windows:

# [1,4,2] -> max=4 ✅
# [4,2,3] -> max=4 ✅
# [2,3,6] -> max=6 ✅

# Output:

# 3

import collections

def solve(nums: list[int], window_size: int) -> int:
    lb = 0
    ans = 0     # to store count of all valid windows
    monotonic_decreasing_dq: collections.deque[int] = collections.deque()    # store indices of even elements in valid window
    for ub in range(len(nums)):
        # prepare monotonic decreasing deque
        while monotonic_decreasing_dq and nums[monotonic_decreasing_dq[-1]] < nums[ub]:
            monotonic_decreasing_dq.pop()
        # build state
        monotonic_decreasing_dq.append(ub)
        # shrink window (update state if needed)
        if ub - lb + 1 > window_size:
            lb += 1
        # remove outdated elements from monotonic deque
        while monotonic_decreasing_dq and monotonic_decreasing_dq[0] < lb:
            monotonic_decreasing_dq.popleft()
        # evaluate
        if ub - lb + 1 == window_size:
            if monotonic_decreasing_dq:
                ans += int(not (nums[monotonic_decreasing_dq[0]] & 1))
    return ans

print(solve([1,4,2,3,6], 3))