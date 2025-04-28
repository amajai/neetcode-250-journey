"""
Difficulty: [Easy]
NeetCode #: [4/250]
Date Solved: [21/04/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- Find the difference between target and the number in the array. Use hashmaps to the record the number with its array index (val: index) you passed in an array.
when you find the diff, check if the number is in the hashmap. 

Time Complexity: O(n)
Space Complexity: O(n)

Key Insights:
- Find the difference and save in it in hashmaps.
"""

def twoSum(nums, target: int):
    prevMap = {} # val: index

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[nums[i]] = i
