"""
Difficulty: [Easy]
NeetCode #: [23/250]
Date Solved: [29/04/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- Have one pointer on the very left and one on the very right. Switch the number with each other and move pointer closer to the middle
until the left pointer passes the right pointer.

Time Complexity: O(n)
Space Complexity: O(n) or O(1)

Key Insights:
- Can even use recursion to solve it.
"""

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    head = 0
    tail = len(s) - 1
    while head < tail:
        temp = s[tail]
        s[tail] = s[head]
        s[head] = temp
        head += 1
        tail -= 1
