# First Repeating Element in Every Window of Size K
# nums = [1, 2, 1, 3, 2]
# k = 3

# Windows:

# [1,2,1] -> 1
# [2,1,3] -> -1
# [1,3,2] -> -1

# Output:

# [1, -1, -1]

"""
nums = [1, 2, 1]
fm = {1: 2, 2: 1}
dq = [0]

nums = [2, 1, 3]
fm = {2: 1, 1: 1, 3: 1}
dq = []

nums = [1, 3, 2]
fm = {1: 1, 3: 1, 2: 1}
dq = []
"""


from collections import Counter, deque

def solve(nums: list[int], k: int) -> list[int]:
    result: list[int] = []                  # to store first repeating element in window
    lb = 0
    freq_counter: Counter[int] = Counter()  # to store freq of elements in window
    repeaters_dq: deque[int] = deque()      # to store indices of first repeated element in dq

    for ub in range(len(nums)):
        # expand window & update state (if needed)
        freq_counter[nums[ub]] += 1
        # pick all the candidates only to remove them lazily
        repeaters_dq.append(ub)

        # shrink window (& update state(s) if needed)
        if ub - lb + 1 > k:
            freq_counter[nums[lb]] -= 1
            if freq_counter[nums[lb]] == 0:
                del freq_counter[nums[lb]]
            lb += 1
        # remove outdated candidates from window
        while repeaters_dq and repeaters_dq[0] < lb:
            repeaters_dq.popleft()
        # clean the candidates lazily to get first non repeating
        while repeaters_dq and freq_counter[nums[repeaters_dq[-1]]] < 2:
            repeaters_dq.popleft()
        
        # evaluate when we hit window
        if ub - lb + 1 == k:
            if repeaters_dq:
                result.append(nums[repeaters_dq[0]])
            else:
                result.append(-1)
    return result

print(solve([1, 2, 1, 3, 2], 3))