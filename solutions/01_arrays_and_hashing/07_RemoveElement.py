"""
Difficulty: [Easy]
NeetCode #: [7/250]
Date Solved: [29/04/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- Using two pointer, one at the start k and the other for looping i. When coming across a num in the array that is equal to the val
you ignore. When num not equal the val, you replace the num at index k with num at index i, then increment k.

Time Complexity: O(n)
Space Complexity: O(1)

Key Insights:
- Have two pointers
"""
def removeElement(nums, val) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
