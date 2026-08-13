# Find First Negative Integer in Every Window of Size K

# Example:

# nums = [12,-1,-7,8,-15,30,16,28]
# k = 3

# Output:

# [-1,-1,-7,-15,-15,0]


# SOLUTIONS
# =========


# 1. BRUTE FORCE
# ==============
# def solve(nums: list[int], k: int) -> None:
#     result: list[int] = []
#     for i in range(len(nums)-k+1):
#         negatives = [num for num in nums[i:i+k] if num < 0]
#         ans = 0 if not negatives else negatives[0]
#         result.append(ans)
#     print(result)



# 2. OPTIMISED (SLIDING WINDOW)
from collections import deque
def solve(nums: list[int], k: int) -> None:
    lb = 0
    negatives: deque[int] = deque() # to store all negatives in a window
    result: list[int] = []
    for ub in range(len(nums)):
        if nums[ub] < 0:
            negatives.append(ub)    # store indices (not value) why?? 

        # shrink the window conditionally
        while ub - lb + 1 > k:
            lb += 1

        # remove negatives that are no longer in window
        while negatives and negatives[0] < lb:
            negatives.popleft()

        # evaluate when we hit a window
        if ub - lb + 1 == k:
            if negatives:
                result.append(nums[negatives[0]])
            else:
                result.append(0)
    print(result)


            

solve([12,-1,-7,8,-15,30,16,28], 3)