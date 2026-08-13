# First Unique Element in Every Window of Size K

# Given:

# nums = [1,2,1,3,2]
# k = 3

# Windows:

# [1,2,1] -> 2
# [2,1,3] -> 2
# [1,3,2] -> 1

# Output:

# [2,2,1]

import collections

def solve(nums: list[int], k: int) -> list[int]:
    lb = 0
    freq_counter: collections.Counter[int] = collections.Counter()  # to store freq of elements in window
    uniques_dq: collections.deque[int] = collections.deque()        # to store indices of elements in window
    result: list[int] = []                                          # to store first unique element in window

    for ub in range(len(nums)):
        freq_counter[nums[ub]] += 1
        uniques_dq.append(ub)

        # shrink window (& update state if needed)
        if ub - lb + 1 > k:
            freq_counter[nums[lb]] -= 1
            if freq_counter[nums[lb]] == 0:
                del freq_counter[nums[lb]]
            lb += 1

        # update state by removing outdated candidates
        while uniques_dq and uniques_dq[0] < lb:
            uniques_dq.popleft()
        # # update state by removing invalid candidates
        # # THIS IS WRONG BECAUSE A NON-UNIQUE ELEMENT IN A WINDOW MIGHT BECOME UNIQUE IN NEXT WINDOW SO WE SHOULD NOT DROP IT
        # # IT FOLLOWS: UNIQUE -> NON-UNIQUE -> UNIQUE ....
        # while uniques_dq and freq_counter[nums[uniques_dq[0]]] > 1:
        #     uniques_dq.popleft()
        # evaluate on window hit
        if ub - lb + 1 == k:
            is_present = False
            for i in uniques_dq:
                if freq_counter[nums[i]] == 1:
                    result.append(nums[i])
                    is_present = True
                    break
            if not is_present:
                result.append(-1)

    return result

print(solve([1, 2, 1, 3, 2], 3))


# OPTIMISED SOLUTION -
# ==================

# from collections import Counter, defaultdict, deque


# def solve(nums: list[int], k: int) -> list[int]:
#     lb = 0
#     freq: Counter[int] = Counter()
#     positions: defaultdict[int, deque[int]] = defaultdict(deque)
#     unique_dq: deque[int] = deque()
#     result: list[int] = []

#     for ub in range(len(nums)):
#         # expand window

#         x = nums[ub]
#         freq[x] += 1
#         positions[x].append(ub)
#         if freq[x] == 1:
#             unique_dq.append(ub)

#         # shrink window
#         if ub - lb + 1 > k:
#             old = nums[lb]
#             freq[old] -= 1
#             positions[old].popleft()

#             # old value became unique again
#             if freq[old] == 1:
#                 unique_dq.append(positions[old][0])

#             if freq[old] == 0:
#                 del freq[old]

#             lb += 1

#         # cleanup candidates

#         while (
#             unique_dq
#             and (
#                 unique_dq[0] < lb
#                 or freq[nums[unique_dq[0]]] != 1
#             )
#         ):
#             unique_dq.popleft()

#         # evaluate

#         if ub - lb + 1 == k:
#             if unique_dq:
#                 result.append(nums[unique_dq[0]])
#             else:
#                 result.append(-1)

#     return result

