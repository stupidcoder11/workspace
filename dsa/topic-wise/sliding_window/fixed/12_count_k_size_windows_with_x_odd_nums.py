# Problem: Count Windows of Size K Having Exactly X Odd Numbers

# Given an integer array nums, an integer window_size, and an integer x.

# Return the number of windows of size window_size that contain exactly x odd numbers.

# Example 1
# nums = [1, 2, 3, 4, 5]
# window_size = 3
# x = 2

# Windows:

# [1,2,3] -> 2 odds ✅
# [2,3,4] -> 1 odd
# [3,4,5] -> 2 odds ✅

# Answer:

# 2


# Example 2
# nums = [2,4,6,8]
# window_size = 2
# x = 1

# Windows:

# [2,4] -> 0 odds
# [4,6] -> 0 odds
# [6,8] -> 0 odds

# Answer:

# 0


# Example 3
# nums = [1,3,5,7]
# window_size = 2
# x = 2

# Windows:

# [1,3] -> 2 odds ✅
# [3,5] -> 2 odds ✅
# [5,7] -> 2 odds ✅

# Answer:

# 3


def solve(nums: list[int], window_size: int, x: int) -> int:
    lb = 0
    rodd = 0    # to store the running odd count of the current window
    ans = 0     # to store the count of valid windows
    for ub in range(len(nums)):
        # build state(s) i.e. add contribution of the item in current window
        rodd += nums[ub] & 1
        # shrink window (& update state(s)) if needed
        if ub - lb + 1 > window_size:
            # remove contribution of items from the old window
            rodd -= nums[lb] & 1
            lb += 1
        # evaluate on window hit
        if ub - lb + 1 == window_size:
            ans += rodd == x
    return ans

solve([1, 2, 3, 4, 5], 3, 2)
solve([2,4,6,8], 2, 1)
solve([1,3,5,7], 2, 2)