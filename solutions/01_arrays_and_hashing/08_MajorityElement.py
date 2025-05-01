"""
Difficulty: [Easy]
NeetCode #: [8/250]
Date Solved: [01/05/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- When loop through the numbers, keep track of the count in hashmap or using Boyer-Moore Voting Algorithm

Time Complexity: O(n)
Space Complexity: O(n) and O(1) without using hashmap

Key Insights:
- Boyer-Moore Voting Algorithm is effective only when majority number is more than [(array size)/2] times.
"""

# Solution 1
def majorityElement(nums) -> int:
    count = {}
    maxCount = res = 0
    for n in nums:
        count[n] = 1 + count.get(n, 0)
        if count[n] > maxCount:
            maxCount = count[n]
            res = n
    return res

# Solution 2: O(1) space
def majorityElement(nums) -> int:
    res = count = 0
    for n in nums:
        if count == 0:
            res = n
        count += (1 if res == n else -1)
    return res
