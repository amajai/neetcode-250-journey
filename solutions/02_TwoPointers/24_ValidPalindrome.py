"""
Difficulty: [Easy]
NeetCode #: [24/250]
Date Solved: [08/05/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- Have two pointer l, r. Compare both the l and r characters. If they are the same continue with the next number.

Time Complexity: O(n)
Space Complexity: O(1)

Key Insights:
- Use two pointers
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isAlphaNum(c):
            return(
                ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')
            )

        while l < r:
            while l < r and not isAlphaNum(s[l]):
                l += 1
            while l < r and not isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True