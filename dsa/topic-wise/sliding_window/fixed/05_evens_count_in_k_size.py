# Count Even Numbers in Every Window of Size K

# Given:

# nums = [1,2,4,5,6]
# k = 3

# Return:

# [2,2,2]

# because:

# [1,2,4] -> 2 evens
# [2,4,5] -> 2 evens
# [4,5,6] -> 2 evens

def solve(nums: list[int], k: int) -> None:
    curr_even_count = 0
    lb = 0
    ans: list[int] = []
    for ub in range(len(nums)):
        # expand window
        curr_even_count += 1 if nums[ub] & 1 == 0 else 0
        # shrink window
        while ub - lb + 1 > k:
            curr_even_count -= 1 if nums[lb] & 1 == 0 else 0
            lb += 1
        # evaluate
        if ub - lb + 1 == k:
            ans.append(curr_even_count)
    print(ans)

solve([1,2,4,5,6], 3)