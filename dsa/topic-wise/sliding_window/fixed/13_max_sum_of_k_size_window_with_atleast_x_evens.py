# Maximum Sum Window of Size K Having At Least X Even Numbers

# Given an integer array nums, an integer window_size, and an integer x.

# Find the maximum sum among all windows of size window_size that contain at least x even numbers.

# If no such window exists, return 0.

# Example 1
# nums = [2,1,4,3,6]
# window_size = 3
# x = 2

# Windows:

# [2,1,4]
# sum = 7
# evens = 2
# ✅ valid

# [1,4,3]
# sum = 8
# evens = 1
# ❌ invalid

# [4,3,6]
# sum = 13
# evens = 2
# ✅ valid

# Answer:

# 13


# Example 2
# nums = [1,3,5,7]
# window_size = 2
# x = 1

# Windows:

# [1,3]
# [3,5]
# [5,7]

# All have:

# 0 evens

# No valid window.

# Answer:

# 0


# Example 3
# nums = [2,4,6,8]
# window_size = 2
# x = 2

# Windows:

# [2,4] -> sum = 6
# [4,6] -> sum = 10
# [6,8] -> sum = 14

# All valid.

# Answer:

# 14

def solve(nums: list[int], window_size: int, x: int) -> int:
    ans = 0    # to store the max sum of valid window (initialized with 0 since problem states to return 0 if no valid window)
    rsum = 0    # to store the running sum of valid window
    reven = 0   # to store the running count of evens in valid window
    
    lb = 0
    for ub in range(len(nums)):
        # expand window & build state
        rsum += nums[ub]
        reven += nums[ub] & 1 == 0
        # shrink window (& update state) if needed
        if ub - lb + 1 > window_size:
            rsum -= nums[lb]
            reven -= nums[lb] & 1 == 0
            lb += 1
        # evaluate
        if ub - lb + 1 == window_size:
            if reven >= x:
                ans = max(ans, rsum)
    return ans

print(solve([2,1,4,3,6], 3, 2))
print(solve([1,3,5,7], 2, 1))
print(solve([2,4,6,8], 2, 2))