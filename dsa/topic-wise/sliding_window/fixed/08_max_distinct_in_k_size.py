# Maximum Number of Distinct Elements in Any Window of Size K

# Example:

# nums = [1,2,1,3,4]
# k = 3

# Windows:

# [1,2,1] -> 2
# [2,1,3] -> 3
# [1,3,4] -> 3

# Answer:

# 3

def solve(nums: list[int], k: int):
    lb = 0
    freq_counter: dict[int, int] = {}
    ans = 0
    for ub in range(len(nums)):
        freq_counter[nums[ub]] = freq_counter.get(nums[ub], 0) + 1
        while ub - lb + 1 > k:
            freq_counter[nums[lb]] -= 1
            if freq_counter[nums[lb]] == 0:
                del freq_counter[nums[lb]]
            lb += 1
        if ub - lb + 1 == k:
            ans = max(ans, len(freq_counter))
    print(ans)

solve([1,2,1,3,4], 3)