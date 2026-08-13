# 3. Count Distinct Elements in Every Window of Size K

# Example:

# nums = [1,2,1,3,4,2,3]
# k = 4

# Output:

# [3,4,4,3]

# because:

# [1,2,1,3] -> {1,2,3}
# [2,1,3,4] -> {1,2,3,4}
# [1,3,4,2] -> {1,2,3,4}
# [3,4,2,3] -> {2,3,4}

# State:

# freq_map
# distinct_count

def solve(nums: list[int], k: int) -> None:
    lb = 0
    ans: dict[int, int] = {}
    result: list[int] = []
    for ub in range(len(nums)):
        # expand window
        ans[nums[ub]] = ans.get(nums[ub], 0) + 1
        # shrink window
        while ub - lb + 1 > k:
            ans[nums[lb]] -= 1
            if ans[nums[lb]] == 0:
                del ans[nums[lb]]
            lb += 1
        # evaluate window
        if ub - lb + 1 == k:
            result.append(len(ans))
    print(result)

solve([1,2,1,3,4,2,3], 4)