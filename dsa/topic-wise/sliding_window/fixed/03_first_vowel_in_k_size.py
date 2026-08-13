# Return the first vowel in every substring of length k.

# Example:

# s = "abecid"
# k = 3

# Windows:

# "abe" -> 'a'
# "bec" -> 'e'
# "eci" -> 'e'
# "cid" -> 'i'

# Expected:

# ['a', 'e', 'e', 'i']
from collections import deque
def solve(s: str, k: int) -> None:
    '''
    Approach
    ========
    01 - iterate through all the elements
    02 - check if the current element is vowel
    03 - if 02 is true then add the index in a deque (say vowel_indices)
    04 - if the window size is more than k, then shrink it
    05 - if the elements in vowel_indices do not belong to window, then remove the left most aka popleft
    06 - if the window size is equal to k and vowel_indices deque is non-empty, append ans with the element in s at the first element of vowel indices
    07 - if vowel_indices is empty, then append 0 to the ans
    '''
    lb = 0
    VOWEL_SET = set('aeiou')
    vowel_indices: deque[int] = deque()     # to store vowels falling in every window
    result: list[str] = []                  # to store first vowel for every window of size k
    for ub in range(len(s)):
        # append the state
        if s[ub] in VOWEL_SET:
            vowel_indices.append(ub)
        # shrink window conditionally
        while ub - lb + 1 > k:
            lb += 1
        # update state (remove outdated values from state which don't fall in that window)
        while vowel_indices and vowel_indices[0] < lb:
            vowel_indices.popleft()
        # evaluate once window size is reached
        if ub - lb + 1 == k:
            if vowel_indices:
                result.append(s[vowel_indices[0]])
            else:
                result.append('')
    print(result)

solve("abecidjk", 3)