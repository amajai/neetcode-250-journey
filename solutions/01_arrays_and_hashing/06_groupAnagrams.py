"""
Difficulty: [Medium]
NeetCode #: [6/250]
Date Solved: [27/04/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- Pass through each word in the array and for each you pass, create a key - value and to hashmap. Key is the array of character
index is count of character in a word and the value is array of words with same characters. 

Time Complexity: O(n * m) # n is length of strings and m is length of shortest string (pref)
Space Complexity: O(1) # No space/storage used

Key Insights:
- Get the ascii of the characters between letter a to z, find the difference between character your at with letter "a" to get index position
which is then set in the array of characters
"""

def groupAnagrams(strs):
    res = {}

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
            
        key = tuple(count)
        if key not in res:
            res[key] = []
        res[key].append(s)
    return res.values()

