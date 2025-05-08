"""
Difficulty: [Medium]
NeetCode #: [12/250]
Date Solved: [08/05/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- There are only 3 digits, 1, 2 and 3. Use three pointers. One at the left (l), right (r) and that goes through the nums (i). When a number is 1,
swap current number with left pointer and increment. If number is 2, swap with right pointer and decrement both it and i.

Time Complexity: O(n)
Space Complexity: O(1)

Key Insights:
- Use Three pointers instead of merge sort.
- Space comp. most be 1.
"""

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r, i = 0, len(nums) - 1, 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1