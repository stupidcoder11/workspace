# Problem: First Even Number in Every Window of Size K
# Given:

# nums = [1, 3, 2, 4, 5, 6]
# k = 3

# Return:

# [2, 2, 2, 4]

# Explanation:

# [1,3,2] -> 2
# [3,2,4] -> 2
# [2,4,5] -> 2
# [4,5,6] -> 4

# If no even exists:

# 0

from collections import deque
def solve(nums: list[int], k: int) -> None:
    '''
    Approach
    ========
    01 - Loop through the elements
    02 - If current element is even, store it's index in a deque
    03 - If the window size is more than k, shrink it
    04 - If the even inside the deque is not from the same window, popleft it
    05 - If the window size is hit and queue is not empty, then the first element from queue will be the index of first even
    06 - If not 05, then add 0 in the result
    '''
    evens: deque[int] = deque() # to store the indices of evens within window
    lb = 0
    ans: list[int] = list()     # to store first evens of the window
    for ub in range(len(nums)):
        # update state conditionally
        if nums[ub] & 1 == 0:
            evens.append(ub)
        # shrink window if it's more than fixed size
        while ub - lb + 1 > k:
            lb += 1
        # update state if needed
        while evens and evens[0] < lb:
            evens.popleft()
        # evaluate once window size is reached
        if ub - lb + 1 == k:
            if evens:
                ans.append(nums[evens[0]])
            else:
                ans.append(0)
    print(ans)
    
    


solve([1, 3, 2, 4, 5, 6], 3)