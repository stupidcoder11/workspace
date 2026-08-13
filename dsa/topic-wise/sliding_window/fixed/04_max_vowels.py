# Problem 3: Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel characters in any substring of length k.

# Vowels are:

# a, e, i, o, u
# Example 1
# Input:
# s = "abciiidef"
# k = 3

# Output:
# 3

# Explanation:

# "abc" -> 1 vowel
# "bci" -> 1 vowel
# "cii" -> 2 vowels
# "iii" -> 3 vowels
# "iid" -> 2 vowels
# "ide" -> 2 vowels
# "def" -> 1 vowel

# Maximum = 3
import math

def solve(s: str, k: int) -> None:
    lb = 0
    curr_vowel_cnt = 0      # current vowel count
    ans = -math.inf
    vowels = set('aeiou')
    for ub in range(len(s)):
        # expand window
        curr_vowel_cnt += 1 if s[ub] in vowels else 0
        # shrink window
        while ub - lb + 1 > k:
            curr_vowel_cnt -= 1 if s[lb] in vowels else 0
            lb += 1
        # evaluate
        if ub - lb + 1 == k:
            ans = max(ans, curr_vowel_cnt)
    print(ans)


solve('abciiidef', 3)
solve('aeiou', 2)
solve("leetcode", 3)
