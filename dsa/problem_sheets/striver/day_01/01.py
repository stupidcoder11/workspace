'''
Given a list of integers containing 0s, 1s and 2s only.
Write a program to sort them in ascending order (without extra space or sorting algo)
'''
from typing import List

# def solve(nums: List[int]) -> None:
#     nums.sort()


# def solve(nums: List[int]) -> None:
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i] > nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]


# def solve(nums: List[int]) -> List[int]:
#     zeros: List[int] = []
#     ones: List[int] = []
#     twos: List[int] = []
#     for num in nums:
#         if num == 0:
#             zeros.append(num)
#         elif num == 1:
#             ones.append(num)
#         else:
#             twos.append(num)
#     return zeros + ones + twos
    
            
def solve(nums: List[int]) -> None:
    curr = 0
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] == 0:
            nums[curr], nums[i] = nums[i], nums[curr]
            curr += 1
            i += 1
        elif nums[i] == 2:
            nums[j], nums[i] = nums[i], nums[j]
            j -= 1
        else:
            i += 1


nums = [0, 2, 2, 1, 1]
solve(nums) # [0, 1, 1, 2, 2]
print(nums)